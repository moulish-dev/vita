from kani_tts import KaniTTS 
import os
from rich.console import Console

console = Console()

class VitaKaniTTS:
    def __init__(self, model_id: str = "nineninesix/kani-tts-370m", **kwargs):
        default_cfg = dict(
            temperature=0.7,           # Control randomness (default: 1.0)
            top_p=0.9,                 # Nucleus sampling (default: 0.95)
            max_new_tokens=2000,       # Max audio length (default: 1200)
            repetition_penalty=1.2,    # Prevent repetition (default: 1.1)
            suppress_logs=False,        # Suppress library logs (default: True)
            show_info=True,            # Show model info on init (default: True)
        )

        default_cfg.update(kwargs)

        # IMPORTANT: store on self
        self.model = KaniTTS(model_id, **default_cfg)
    

    def generate_audio(self, text, output_path="output.wav"):
        os.makedirs(os.path.dirname(output_path), exist_ok=True) if "/" in output_path else None

        console.print("[bold red] Generating audio.....[/]")
        # Generate audio from text
        audio, text = self.model(text)

        # Save to file (requires soundfile)
        self.model.save_audio(audio, output_path)
        console.print("[bold green] Finished Generating audio.....[/]")

        return output_path, text

