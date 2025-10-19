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
        model_id: str = "suno/bark-small",          # or "suno/bark"
        voice_preset: str = "v2/en_speaker_6",
        device: str | None = None,                  # "cuda" or "cpu"; auto if None
        fp16: bool = True,                          # load in half precision if supported
        flash_attn2: bool = False,                  # requires 'flash-attn' installed
        cpu_offload: bool = False,                  # requires 'accelerate' installed
        **kwargs,                                   # tolerate extras from factory
    ):
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = device
        self.voice_preset = voice_preset

        # dtype choice (fp16 only on CUDA/XPU)
        use_fp16 = fp16 and (device != "cpu")
        dtype = torch.float16 if use_fp16 else None

        console.print(f"[bold cyan]Loading Bark: {model_id} on {device} "
                      f"(fp16={use_fp16}, flash2={flash_attn2}, offload={cpu_offload})...[/]")

        attn_impl = "flash_attention_2" if (flash_attn2 and device != "cpu") else None
        attn_kw = {"attn_implementation": attn_impl} if attn_impl else {}

        self.processor = AutoProcessor.from_pretrained(model_id)
        self.model = BarkModel.from_pretrained(model_id, dtype=dtype, **attn_kw).to(device)

        # OPTIONAL: offload sub-models to CPU when idle (saves VRAM; needs 'accelerate')
        if cpu_offload and device != "cpu":
            try:
                self.model.enable_cpu_offload()
            except Exception as e:
                console.print(f"[bold yellow]CPU offload not enabled ({e}). Continuing...[/]")

        # Silence pad/attention warnings: set pad_token_id = eos_token_id
        gen = self.model.generation_config
        if getattr(gen, "pad_token_id", None) is None and getattr(gen, "eos_token_id", None) is not None:
            gen.pad_token_id = gen.eos_token_id

        # Mirror pad token on processor tokenizer if present
        tok = getattr(self.processor, "tokenizer", None)
        if tok is not None and getattr(tok, "pad_token_id", None) in (None, -1):
            if getattr(tok, "eos_token_id", None) is not None:
                tok.pad_token_id = tok.eos_token_id

        self.sample_rate = int(getattr(gen, "sample_rate", 24_000))
        console.print("[bold green]Bark loaded successfully![/]")

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