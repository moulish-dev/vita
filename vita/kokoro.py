from kokoro import KPipeline
import soundfile as sf
import os
import shutil
import platform

class KokoroTTS:
    def __init__(self, lang_code='a',voice='af_heart', repo_id="hexgrad/Kokoro-82M"):
        self.pipeline = KPipeline(repo_id, lang_code)
        self.voice = voice
    
    def generate_audio(self, text, output_path="output.wav"):
        check_espeak()
        os.makedirs(os.path.dirname(output_path), exist_ok=True) if "/" in output_path else None
        generator = self.pipeline(text, voice=self.voice)
        for i, (_, _, audio) in enumerate(generator):
            sf.write(output_path, audio, samplerate=24000)
            break

# important for Kokoro
def check_espeak():
    system = platform.system()
    if system in ["Linux", "Darwin"]:
        if not shutil.which("espeak-ng"):
            print("⚠️  Warning: 'espeak-ng' not found in your system PATH.")
            print("   → Some Kokoro models may not work without it.")
            print("   → To install on Linux: sudo apt install espeak-ng")
            print("   → On macOS: brew install espeak")
            print()
    elif system == "Windows":
        print("ℹ️  On Windows, make sure 'espeak-ng' is installed and added to your PATH.")
        print("   → Download: https://github.com/espeak-ng/espeak-ng/releases")
        print()