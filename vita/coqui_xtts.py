from TTS.api import TTS as CoquiTTS
import os
import torch
from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig, XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
from rich.console import Console
from rich.progress import track

console = Console()

# Adding XttsConfig to PyTorch's safe global list
add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

class XTTS:
    def __init__(self, speaker_wav=None, language="en"):
        gpu_bool = torch.cuda.is_available() # checks if gpu is there or not
        self.tts = CoquiTTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=gpu_bool)
        self.speaker_wav = speaker_wav
        self.language = language
    
    def generate_audio(self, text, output_path="output.wav"):
        if not self.speaker_wav:
            raise ValueError("🔊 XTTS requires a speaker_wav file for voice cloning.")
        os.makedirs(os.path.dirname(output_path), exist_ok=True) if "/" in output_path else None
        console.print("[bold green] Generating audio.....[/]")
        self.tts.tts_to_file(
            text = text,
            file_path = output_path,
            speaker_wav = self.speaker_wav,
            language=self.language
        )