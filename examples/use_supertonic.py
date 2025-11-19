# Examples : Use Kokoro Text to Speech Model

from vita import VitaTTS

text = "Artificial intelligence is transforming how humans interact with machines, making communication faster, more natural, and deeply personal."
text1="This is an example of the Kokoro Text to Speech model"

tts = VitaTTS( model="supertonic")
tts.generate_audio(
    text=text, 
    output_path="supertonic_demo.wav"
    )