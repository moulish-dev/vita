# import pytest
# from vita.coqui_xtts import XTTS
# import os


# SAMPLE_SPEAKER = "samples/hello.wav"

# @pytest.mark.skip(reason="XTTS model loading crashes on Windows due to transformer unsafe deserialization.")
# def test_xtts_raises_error_without_speaker():
#     with pytest.raises(ValueError):
#         tts = XTTS()
#         tts.generate_audio("This should fail", "out.wav")

# @pytest.mark.skipif(not os.path.exists(SAMPLE_SPEAKER), reason="Sample speaker wav not found.")
# def test_xtts_generate_audio_creates_file(tmp_path):
#     output_file = tmp_path / "xtts_test.wav"
#     tts = XTTS(speaker_wav=SAMPLE_SPEAKER, language="en")
    
#     tts.generate_audio("Testing XTTS voice cloning.", str(output_file))

#     assert output_file.exists(), "XTTS did not generate an audio file"
#     assert os.path.getsize(output_file) > 1000, "Generated XTTS file is too small (likely failed)"
