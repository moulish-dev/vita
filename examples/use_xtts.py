# examples/use_xtts.py

from vita import TTS

tts = TTS(
    model="xtts",
    speaker_wav="samples/hello.wav",  # path to your speaker sample
    language="en"
)

tts.generate_audio("Hello! This is XTTS speaking through VITA.", output_path="xtts_output.wav")
