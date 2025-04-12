import argparse
from vita import TTS
from .kokoro import check_espeak

def main():
    check_espeak()
    
    parser = argparse.ArgumentParser(description="VITA CLI - Voice Integration Toolkit for Applications")
    parser.add_argument("--text", required=True, help="Text to speech")
    parser.add_argument("--output", default="output.wav", help="Name of the output .wav file")
    parser.add_argument("--model", default="kokoro", choices=["kokoro","xtts"], help="TTS model to use")
    parser.add_argument("--speaker_wav", help="Speaker reference audio (for XTTS)")
    parser.add_argument("--language", default="en", help="Language code (for XTTS)")
    args = parser.parse_args()
    
    tts = TTS(
        model=args.model,
        speaker_wav=args.speaker_wav,
        language=args.language
    )
    tts.generate_audio(args.text, args.output)
    
    
if __name__ == "__main__":
    main()