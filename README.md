
---

# 🎙️ VITA – Voice Integration Toolkit for Applications

**VITA** is a developer-friendly Python library that makes it easy to integrate TTS (Text-to-Speech) into your applications.  
Powered by open-weight models like **[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)**, VITA is modular, lightweight, and ready for production or personal use.

---

## 🚀 Features

- ✅ Seamless Python API  
- ✅ One-line CLI usage  
- ✅ Outputs clean `.wav` files  
- ✅ Based on [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)  
- ✅ Designed for plug-and-play integration  
- 🔜 Multi-model support coming soon  

---

## 📦 Installation

Python Version - 3.11

```bash
git clone https://github.com/moulish-dev/vita.git
cd vita
pip install -r requirements.txt
pip install -e .
```

---

## 🛠️ System Requirements

VITA uses the `kokoro` TTS engine, which may rely on `espeak-ng` for phoneme processing on some platforms.

### 🐧 Linux

```bash
sudo apt-get update
sudo apt-get install espeak-ng
```

### 🪟 Windows

- Download `espeak-ng` from [Releases](https://github.com/espeak-ng/espeak-ng/releases)  
- Run the installer (`espeak-ng-setup.exe`)  
- Add it to your **System PATH**

### 🍏 macOS

```bash
brew install espeak
```

---

## 🧠 Usage

### 🔧 Python

```python
from vita import TTS

tts = TTS()
tts.generate_audio("This is VITA speaking.", output_path="demo.wav")
```

### 📟 CLI

```bash
python -m vita --text "Hello from VITA!" --output hello.wav
```

---

## 🧪 Example

```bash
python examples/use_vita.py
```

---

## 🔭 Roadmap

- 🔜 Add Bark, Tortoise, and Coqui TTS support  
- 🔜 REST API interface with FastAPI  
- 🔜 Speaker identity and voice styling  
- 🔜 Gradio/Streamlit web demo  

---

## 📜 License

Apache 2.0 — use freely in personal and commercial applications.
![License](https://img.shields.io/github/license/moulish-dev/vita?style=flat-square)
---

## 🙌 Acknowledgements

- Kokoro-82M by [Hexgrad](https://huggingface.co/hexgrad)  
- Built using [KPipeline](https://github.com/hexgrad/kokoro)

---
