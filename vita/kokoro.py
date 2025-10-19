from kokoro import KPipeline
import soundfile as sf
import os
from rich.console import Console
from rich.progress import track

console = Console()

class KokoroTTS:
    def __init__(self, lang_code='a',voice='af_heart', repo_id="hexgrad/Kokoro-82M", **kwargs):
        self.pipeline = KPipeline(lang_code, repo_id)
        self.voice = voice
    
    def generate_audio(self, text, output_path="output.wav"):
        os.makedirs(os.path.dirname(output_path), exist_ok=True) if "/" in output_path else None

        console.print("[bold red] Generating audio.....[/]")
        generator = self.pipeline(text, voice=self.voice)
        for i, (_, _, audio) in enumerate(generator):
            sf.write(output_path, audio, samplerate=24000)
            break
        console.print("[bold green] Finished Generating audio.....[/]")

