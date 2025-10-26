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

        
    
    def generate_audio(self, text, output_path="output.wav", ref_text = "samples/dave.txt", ref_audio_path = "samples/dave.wav"):

        console.print("[bold red] Generating audio.....[/]")
        ref_text = open(ref_text, "r").read().strip()
        ref_codes = self.tts.encode_reference(ref_audio_path)

        wav = self.tts.infer(text, ref_codes, ref_text)
        sf.write(output_path, wav, 24000)
        console.print("[bold green] Finished Generating audio.....[/]")

    

