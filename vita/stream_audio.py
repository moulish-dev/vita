# Simulated Streaming for models with no streaming support

import sounddevice as sd
import soundfile as sf
import numpy as np
import uuid
import os
import time

from vita import TTS

import warnings
# Suppress known non-critical warnings
warnings.filterwarnings("ignore", category=UserWarning, message="dropout option adds dropout")
warnings.filterwarnings("ignore", category=FutureWarning, message=".*weight_norm.*")

def stream_tts(text, chunk_size=20, model="kokoro", speaker_wav=None):
    # splitting the text
    sentences = text.split(".")
    tts = TTS(model=model, speaker_wav=speaker_wav)
    
    for sentence in sentences:
        if not sentence.strip():
            continue
        
        # Generate audio for the chunk
        out_file = f"temp_chunk_{uuid.uuid4().hex[:8]}.wav"
        tts.generate_audio(sentence.strip(), out_file)
        
        # Play audio chunk
        audio_data, samplerate = sf.read(out_file, dtype='int16')
        sd.play(audio_data, samplerate=samplerate)
        sd.wait()
        
        time.sleep(0.00001)
        os.remove(out_file)