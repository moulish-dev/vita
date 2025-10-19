from pydub import AudioSegment
import platform, shutil

def convert_to_format(wav_path, target_format="mp3"):
    audio = AudioSegment.from_wav(wav_path)
    out_file = wav_path.replace(".wav", f".{target_format}")
    audio.export(out_file, format=target_format)
    return out_file

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