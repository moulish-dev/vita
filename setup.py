from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="vita",
    version="0.3.2",
    packages=find_packages(),
    python_requires=">=3.10",

    description="VITA - Voice Integration Toolkit for Applications",
    long_description=README,
    long_description_content_type="text/markdown",

    author="Moulish",
    license="Apache-2.0",
    url="https://github.com/moulish-dev/vita",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries",
    ],

    # --- Core dependencies (platform-agnostic) ---
    install_requires=[
        "kokoro>=0.9.2",
        "soundfile>=0.12",
        "sounddevice>=0.4",
        "scipy>=1.10",
        "rich>=13.0",
        "phonemizer>=3.2",   # requires system espeak-ng
    ],

    # --- Optional platform-specific extras ---
    extras_require={
        # Default (safe for all CPUs)
        "cpu": [
            "llama-cpp-python>=0.3.0",
            "torch>=2.3",
        ],

        # Apple Silicon (Metal acceleration)
        "apple-silicon": [
            "torch>=2.3 ; platform_system == 'Darwin' and platform_machine == 'arm64'",
            "llama-cpp-python>=0.3.0 ; platform_system == 'Darwin' and platform_machine == 'arm64'",
        ],

        # Linux aarch64 (e.g., Raspberry Pi 5 / ARM servers)
        "linux-aarch64": [
            "torch>=2.3 ; platform_system == 'Linux' and platform_machine == 'aarch64'",
            "llama-cpp-python>=0.3.0 ; platform_system == 'Linux' and platform_machine == 'aarch64'",
        ],

        # Optional GPU variants for x86_64
        "cuda": [
            "torch>=2.3 ; platform_system == 'Linux' and platform_machine == 'x86_64'",
        ],
        "rocm": [
            "torch>=2.3 ; platform_system == 'Linux' and platform_machine == 'x86_64'",
        ],
    },

    entry_points={
        "console_scripts": [
            "vita = vita.__main__:main",
        ]
    },
)
