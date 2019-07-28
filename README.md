# Audio Transcriber

## Purpose

This audio transcriber is a daemon built on IBM's [watson speech to text](https://www.ibm.com/watson/services/speech-to-text/) service automatically transcribes audio files added to a specified folder. It has only a command line interface.

## Notices

This product includes software originally developed by IBM Corporation
Copyright 2018 IBM Corp.

NOTICE: The watson-developer-cloud python sdk is licensed under the Apache 2.0 license.
Do not distribute it without complying with the license.

#### This application generates a config file for you to add your plain text credentials to, so **DO NOT** commit the config file to a public repository!!!

## Setup

1. Install [git](https://git-scm.com/downloads), [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)
2. Check out this repository and dependencies using the following commands in your terminal:

```
git clone https://github.com/nathanblaubach/transcriber.git
cd transcriber
python3 -m pip install --upgrade -r requirements.txt
python3 src/run.py
```

## Dependencies

* [Python](https://www.python.org/)
* [IBM Speech to Text](https://www.ibm.com/watson/services/speech-to-text/)

## Contributors

* [Nathan Blaubach](https://github.com/nathanblaubach)

## License

[MIT](https://github.com/nathanblaubach/transcriber/blob/master/LICENSE)
