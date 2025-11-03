from .neutts_dev import NeuTTSAir
import soundfile as sf
import os
from rich.console import Console
from rich.progress import track

console = Console()

class NeuttsAirTTS:
    def __init__(
            self,
            backbone_repo="neuphonic/neutts-air-q4-gguf",
            backbone_device="cpu",
            codec_repo="neuphonic/neucodec", 
            codec_device="cpu",
            **kwargs):
        
        self.tts = NeuTTSAir(backbone_repo, backbone_device, codec_repo, codec_device)

    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def close(self):
        # Try the library's own close first (if provided)
        try:
            self.tts.close()
        except AttributeError:
            pass
        # Fallbacks: common internal attrs you might have
        for attr in ("llm", "backbone", "model"):
            obj = getattr(self.tts, attr, None)
            try:
                if obj and hasattr(obj, "close"):
                    obj.close()
            except Exception:
                pass

    
    def generate_audio(self, text, output_path="output.wav", ref_text = "samples/dave.txt", ref_audio_path = "samples/dave.wav"):

        console.print("[bold red] Generating audio.....[/]")
        ref_text = open(ref_text, "r").read().strip()
        ref_codes = self.tts.encode_reference(ref_audio_path)

        wav = self.tts.infer(text, ref_codes, ref_text)
        sf.write(output_path, wav, 24000)
        console.print("[bold green] Finished Generating audio.....[/]")

    

