import pytest
from vita.kokoro import KokoroTTS
import os

@pytest.mark.parametrize("text", [
    "Hello, world!",
    "This is a test of the Kokoro TTS model.",
    "Another quick example."
])
def test_kokoro_generate_audio_creates_file(tmp_path, text):
    output_file = tmp_path / "test.wav"
    tts = KokoroTTS()

    tts.generate_audio(text, str(output_file))

    assert output_file.exists(), "Output file was not created"
    assert os.path.getsize(output_file) > 1000, "Output file seems too small (might be empty)"
