# Examples : Use Kokoro Text to Speech Model

from vita import TTS

tts = TTS( model="kokoro")
tts.generate_audio(
    text="This is an example of the Kokoro Text to Speech model", 
    output_path="kokoro_demo.wav"
    )