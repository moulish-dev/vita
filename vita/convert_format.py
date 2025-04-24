from pydub import AudioSegment

def convert_to_format(wav_path, target_format="mp3"):
    audio = AudioSegment.from_wav(wav_path)
    out_file = wav_path.replace(".wav", f".{target_format}")
    audio.export(out_file, format=target_format)
    return out_file

