from .kokoro import KokoroTTS
from .coqui_xtts import XTTS
import warnings

# Suppress known non-critical warnings
warnings.filterwarnings("ignore", category=UserWarning, message="dropout option adds dropout")
warnings.filterwarnings("ignore", category=FutureWarning, message=".*weight_norm.*")


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