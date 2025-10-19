
---

## 🛣️ VITA – Feature Roadmap

### ✅ MVP (v0.1.0) — *Initial Release*
- [x] Wrapper for **Kokoro-82M** using Hugging Face
- [x] Python API to generate TTS (`tts.generate(text, output_path)`)
- [x] CLI support: `vita --text "Hello"`
- [x] Audio output as `.wav`
- [x] Examples folder with usage script
- [x] Clean project structure and base `TTS` interface

---

### 🚀 v0.2.0 — *Multi-Model Support Framework*
- [x] Add support for additional models (e.g. [Bark](https://github.com/suno-ai/bark), [Tortoise TTS](https://github.com/neonbjb/tortoise-tts), [Coqui TTS](https://github.com/coqui-ai/TTS))
- [x] Modularize `TTS` selection via model registry or factory pattern
- [x] Add config file loading (JSON/YAML)
- [x] Add streaming TTS support (for real-time apps)

---

### 🎛️ v0.3.0 — *Advanced Usability Features*
- [x] Prettified CLI output (with progress bars and color logging)
- [x] Batch mode: Convert a list of sentences at once
- [x] Auto-generate filenames if not provided
- [x] Output to MP3/OGG using `pydub` or `ffmpeg` 

---

### 🌍 v0.4.0 — *Language & Voice Control*
- [ ] Language selection support (if model supports)
- [ ] Voice style/mood selection (e.g., whispering, angry, etc.)
- [ ] Support for speaker embeddings / multi-voice models

---

### 🔒 v0.5.0 — *Developer & Deployment Toolkit*
- [ ] Dockerfile for easy deployment
- [ ] Python package (`pip install kokoro-tts`) setup
- [ ] GitHub Actions for CI/CD
- [ ] VS Code devcontainer (optional for contributors)

---

### 📱 v0.6.0 — *API/Server Integration*
- [ ] FastAPI or Flask server interface
- [ ] REST API: `POST /tts` with JSON body
- [ ] Host on Hugging Face Spaces or Replit for demo

---
