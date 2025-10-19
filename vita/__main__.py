import argparse
from vita import TTS
from .utils import check_espeak, convert_to_format
import datetime
import warnings
from vita.model_config import load_model_configs

def main():
    # Suppress known non-critical warnings
    warnings.filterwarnings("ignore", category=UserWarning, message="dropout option adds dropout")
    warnings.filterwarnings("ignore", category=FutureWarning, message=".*weight_norm.*")
    check_espeak()
    
    parser = argparse.ArgumentParser(description="VITA CLI - Voice Integration Toolkit for Applications")
    parser.add_argument("--text", required=True, help="Text to speech")
    parser.add_argument("--output", default="output.wav", help="Name of the output .wav file")
    parser.add_argument("--model", default="kokoro", choices=["kokoro","bark"], help="TTS model to use")
    parser.add_argument("--speaker_wav", help="Speaker reference audio (for XTTS)")
    parser.add_argument("--language", default="en", help="Language code (for XTTS)")
    parser.add_argument("--stream", action="store_true", help="Simulate streaming TTS (plays audio in chunks)")
    parser.add_argument("--input_file", help="Path to a text file with multiple lines to convert")
    parser.add_argument("--format", choices=["wav", "mp3", "ogg"], default="wav")
    parser.add_argument("--list-models", action="store_true", help="List available TTS models")
    models = load_model_configs()
    model_info = models[args.model]

    # Auto fallback language
    language = args.language or model_info["default_language"]

    # Smart validation
    if model_info["requires_speaker_wav"] and not args.speaker_wav:
        parser.error(f"The model '{args.model}' requires --speaker_wav")

    args = parser.parse_args()
    
    if args.stream:
        from vita.stream_audio import stream_tts
        stream_tts(args.text, model=args.model, speaker_wav=args.speaker_wav)
        return
    
    if not args.output:
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"output_{now}.wav"

    if args.list_models:
        for name, info in models.items():
            print(f"🔹 {name}: {info['description']} (Default lang: {info['default_language']})")
        return
    
    tts = TTS(
        model=args.model,
        speaker_wav=args.speaker_wav,
        language=args.language
    )
    
    if args.input_file:
        with open(args.input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        for idx, line in enumerate(lines):
            filename = f"output_{idx + 1}.wav"
            tts.generate_audio(line, filename)
        return
    
    tts.generate_audio(args.text, args.output)
    if args.format != "wav":
        convert_to_format(args.output, target_format=args.format)

    
if __name__ == "__main__":
    main()