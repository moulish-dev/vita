# Examples : Use Kokoro Text to Speech Model

from vita import TTS

tts = TTS( model="neuttsair")
tts.generate_audio(
    text="This is an example of the NeuTTS-Air Text to Speech model", 
    output_path="neuttsair_demo.wav"
    )