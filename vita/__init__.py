from .kokoro import KokoroTTS
from .coqui_xtts import XTTS

class TTS:
    def __init__(self, model="kokoro", **kwargs):
        if model == "kokoro":
            self.engine = KokoroTTS(**kwargs)
        elif model == "xtts":
            self.engine = XTTS(**kwargs)
        else:
            raise ValueError(f"Model '{model}' not supported")
        
    def generate_audio(self, text, output_path="output.wav"):
        self.engine.generate_audio(text, output_path)