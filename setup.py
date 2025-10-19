from setuptools import setup, find_packages

setup(
    name="vita",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[
        "kokoro>=0.9.2",
        "soundfile"
        "sounddevice"
        "scipy"
    ],
    entry_points={
        "console_scripts": [
            "vita = vita.__main__:main"
        ]
    },
    description="VITA - Voice Integration Toolkit for Applications",
    author="Moulish",
    license="Apache-2.0",
    url="https://github.com/moulish-dev/vita",
)
