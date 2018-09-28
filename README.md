
# Audio Transcriber

## Purpose

This audio transcriber built on IBM's [watson speech to text](https://www.ibm.com/watson/services/speech-to-text/) service automatically transcribes audio files added to a specified folder

## Notices

This product includes software originally developed by IBM Corporation
Copyright 2018 IBM Corp.

NOTICE: The watson-developer-cloud python sdk is licensed under the Apache 2.0 license.
Do not distribute it without complying with the license.

#### This application generates a config file for you to add your plain text credentials to, so **DO NOT** commit the config file to a public repository!!!

## Setup

This project requires the installation of python, pip and tkinter for python3.
On Mac and Windows, the installer at https://www.python.org/ includes tkinter and pip by default.
On Linux, python is likely preinstalled, but you may need to install the python3-pip and python3-tk packages.

```
git clone https://github.com/blaubachn/transcriber.git
cd transcriber
python3 -m pip install --upgrade "watson-developer-cloud>=1.4.0"
python3 src/run.py
```

## License

[MIT](https://github.com/blaubachn/transcriber/blob/master/LICENSE.md)
