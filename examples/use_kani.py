# Examples : Use Kokoro Text to Speech Model

from vita import TTS

from nemo.collections.tts.modules.audio_codec_modules import HiFiGANEncoder
import inspect; print(inspect.signature(HiFiGANEncoder.__init__))


tts = TTS( model="kani")
tts.generate_audio(
    text="This is an example of the Kani Text to Speech model", 
    output_path="kani_demo.wav"
    )