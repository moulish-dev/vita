from .kokoro import KokoroTTS

class TTS:
    def __init__(self, model="kokoro", **kwargs):
        if model == "kokoro":
            self.engine = KokoroTTS(**kwargs)
        else:
            raise ValueError(f"Model '{model}' not supported")
        
    def generate_audio(self, text, output_path="output.wav"):
        self.engine.generate_audio(text, output_path)