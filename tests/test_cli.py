import subprocess
import os
import tempfile
from pathlib import Path

def test_cli_generates_kokoro_audio():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "test.wav"
        result = subprocess.run(
            [
                "python", "-m", "vita",
                "--text", "Testing VITA CLI",
                "--model", "kokoro",
                "--output", str(output_path)
            ],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0, f"CLI failed: {result.stderr}"
        assert output_path.exists(), "Output .wav file was not created"
        assert output_path.stat().st_size > 1000, "Generated .wav file is too small"
        assert "Generating audio" in result.stdout, "Expected message not in CLI output"
