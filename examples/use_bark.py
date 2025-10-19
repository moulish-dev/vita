# examples/use_xtts.py

from vita import TTS

tts = TTS(
    model="bark"
)

tts.generate_audio(
    "Hello! This is BarkTTS speaking through VITA.", 
    output_path="bark_output.wav"
    )
