from .kokoro import KokoroTTS
from .bark import BarkTTS
from .neuttsair import NeuttsAirTTS
from .supertonic import SupertonicTTS
import warnings

# Suppress known non-critical warnings
warnings.filterwarnings("ignore", category=UserWarning, message="dropout option adds dropout")
warnings.filterwarnings("ignore", category=FutureWarning, message=".*weight_norm.*")

# checks if kani-tts(pypi) package is installed or not
try:
    from .kani import VitaKaniTTS
    _HAS_KANI = True
except ImportError:
    VitaKaniTTS = None
    _HAS_KANI = False



class VitaTTS:
    def __init__(self, model="kokoro", **kwargs):
        if model == "kokoro":
            self.engine = KokoroTTS(**kwargs)
        elif model == "bark":
            self.engine = BarkTTS(**kwargs)
        elif model == "neuttsair":
            self.engine = NeuttsAirTTS(**kwargs)
        elif model == "kani":
            if not _HAS_KANI:
                raise ImportError(
                    "VitaKaniTTS requires the 'kani-tts' extra. "
                    "Install it with: pip install vita[kani]"
                )
            self.engine = VitaKaniTTS(**kwargs)
        elif model == "supertonic":
            self.engine = SupertonicTTS(**kwargs)
        else:
            raise ValueError(f"Model '{model}' not supported")
        
    def generate_audio(self, text, output_path="output.wav"):
        self.engine.generate_audio(text, output_path)