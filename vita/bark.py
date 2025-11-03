from transformers import AutoProcessor, BarkModel
import scipy, torch, os
import numpy as np
from rich.console import Console

console = Console()

class BarkTTS:
    """
    Bark via Transformers modelling API.
    - Fixes pad_token/attention_mask warning
    - Optional fp16, flash-attn2, CPU offload
    """
    
    def __init__(
        self,
        model_id: str = "suno/bark-small",
        voice_preset: str = "v2/en_speaker_6",
        device: str | None = None,
        fp16: bool = True,
        flash_attn2: bool = False,
        **kwargs,
    ):
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = device
        self.voice_preset = voice_preset
        self.sample_rate = 24_000

        # decide dtype for loading
        use_fp16 = fp16 and (device != "cpu")
        torch_dtype = torch.float16 if use_fp16 else None

        console.print(
            f"[bold cyan]Loading Bark: {model_id} on {device} "
            f"(fp16={use_fp16}, flash2={flash_attn2})...[/]"
        )

        attn_kw = {}
        if flash_attn2 and device != "cpu":
            attn_kw["attn_implementation"] = "flash_attention_2"

        self.processor = AutoProcessor.from_pretrained(model_id)

        # LOAD with torch_dtype (if any), then move to device
        # Note: pass torch_dtype (not dtype) to from_pretrained
        if torch_dtype is not None:
            self.model = BarkModel.from_pretrained(model_id, torch_dtype=torch_dtype, **attn_kw)
            # ensure model is on the right device and dtype
            self.model = self.model.to(device, dtype=torch_dtype)
        else:
            self.model = BarkModel.from_pretrained(model_id, **attn_kw)
            self.model = self.model.to(device)


    def _prepare_inputs(self, text: str):
        inputs = self.processor(
            text=[text],
            voice_preset=self.voice_preset,
            return_tensors="pt",
        )
        # Explicit attention_mask (all 1s) since we don’t pad here
        if "input_ids" in inputs and "attention_mask" not in inputs:
            inputs["attention_mask"] = torch.ones_like(inputs["input_ids"])
        # Move all tensors to device
        return {k: v.to(self.device) if torch.is_tensor(v) else v for k, v in inputs.items()}

    def generate_audio(self, text: str, output_path: str = "bark_out.wav"):
        console.print("[bold yellow]Generating audio with Bark...[/]")
        inputs = self._prepare_inputs(text)

        with torch.no_grad():
            audio = self.model.generate(
                **inputs,
                # optional generation knobs; defaults are usually fine
                pad_token_id=self.model.generation_config.pad_token_id,
            )

        audio_np = audio.detach().cpu().numpy().squeeze().astype(np.float32)

        if "/" in output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        scipy.io.wavfile.write(output_path, rate=self.sample_rate, data=audio_np)
        console.print(f"[bold green]Done → {output_path}[/]")
        return output_path, self.sample_rate

class BarkTTS_Depreceated:
    """
    Bark Tranformers Pipeline 
    Attention Mask problem detected
    """
    def __init__(self, model_id="suno/bark-small", **kwargs):
        self.processor = AutoProcessor.from_pretrained(model_id)
        self.model = BarkModel.from_pretrained(model_id)
        self.model.to("cuda" if torch.cuda.is_available() else "cpu")
        self.voice_preset = "v2/en_speaker_6"

    def generate_audio(self, text, output_path="output.wav"):
        console.print("[bold red]Generating audio...[/]")
        inputs = self.processor(text, voice_preset=self.voice_preset, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            audio = self.model.generate(**inputs)
        audio = audio.cpu().numpy().squeeze()
        scipy.io.wavfile.write(output_path, rate=self.model.generation_config.sample_rate, data=audio)
        console.print("[bold green]Finished generating audio![/]")