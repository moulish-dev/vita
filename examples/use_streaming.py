# examples/use_streaming.py

from vita.stream_audio import stream_tts

text = "This is an example of simulated streaming text to speech. The audio will play chunk by chunk as it's generated."

# You can also try model="xtts" with a speaker_wav if needed
stream_tts(
    text=text,
    model="kokoro",  # or "xtts"
    speaker_wav=None  # required only for XTTS
)
