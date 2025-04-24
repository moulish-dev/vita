
## 🔧 CLI Usage (VITA)

VITA supports both standard and streaming TTS from the command line.

### 📌 Basic Usage

```bash
python -m vita --text "Hello from VITA"
```

---

### 🎙️ Output to a Specific File

```bash
python -m vita --text "Save this audio" --output demo.wav
```

---

### 🧠 Use XTTS with a Custom Speaker Voice

```bash
python -m vita --text "This is XTTS voice cloning" \
--model xtts \
--speaker_wav samples/your_voice.wav \
--output output_xtts.wav
```

---

### 🌍 Change Language (XTTS only)

```bash
python -m vita --text "Bonjour, comment ça va ?" \
--model xtts \
--speaker_wav samples/french_voice.wav \
--language fr \
--output bonjour.wav
```

---

### 🚀 Simulate Streaming Output (Chunked Playback)

```bash
python -m vita --text "This will play as it's being generated" --stream
```

> ℹ️ Note: `--stream` supports `kokoro` and `xtts`  
> Ensure `--speaker_wav` is provided for `xtts` in streaming mode

---
### Batch coverting a list of sentences from a file

```bash
python -m vita --input_file batch.txt
```

---

### 🧩 All Available CLI Flags

| Flag | Description |
|------|-------------|
| `--text` | (Required) Input text to synthesize |
| `--output` | Output `.wav` file name (default: `output.wav`) |
| `--model` | Choose model: `kokoro` (default) or `xtts` |
| `--speaker_wav` | Path to speaker voice file (required for `xtts`) |
| `--language` | Language code (for `xtts`, default: `en`) |
| `--stream` | Simulate streaming TTS playback |

---

### 🧪 Examples Folder

Try example scripts:

```bash
python examples/use_kokoro.py
python examples/use_xtts.py
python examples/use_streaming.py
```

---

## ✅ Requirements

Make sure `espeak-ng` is installed (for Kokoro):

**Linux:**
```bash
sudo apt install espeak-ng
```

**macOS:**
```bash
brew install espeak
```

**Windows:**  
Download and install from [espeak-ng releases](https://github.com/espeak-ng/espeak-ng/releases)

---
