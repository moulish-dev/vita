# 📦 CHANGELOG

All notable changes to this project will be documented in this file.

---

## [v0.2.0] - 2024-04-23

### Added
- Support for XTTS-v2 (multilingual, speaker cloning)
- Streaming TTS playback with `--stream` flag
- `models.yaml` file to configure TTS models
- CLI validation for model-specific requirements
- Warning suppression for cleaner CLI output

### Fixed
- Windows temp file lock bug in streaming playback

---

## [v0.1.0] - 2024-04-15

### Added
- Initial support for Kokoro-82M TTS model
- Python API: `tts.generate_audio(text, output)`
- CLI: `--text`, `--output`
- Examples folder with basic usage
