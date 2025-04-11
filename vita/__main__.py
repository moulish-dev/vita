import argparse
from vita import TTS
from .kokoro import check_espeak

def main():
    check_espeak()
    
    parser = argparse.ArgumentParser(description="VITA CLI - Voice Integration Toolkit for Applications")
    parser.add_argument("--text", required=True, help="Text to speech")
    parser.add_argument("--output", default="output.wav", help="Name of the output .wav file")
    args = parser.parse_args()
    
    tts = TTS()
    tts.generate_audio(args.text, args.output)
    
    
if __name__ == "__main__":
    main()