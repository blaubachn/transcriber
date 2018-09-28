
# Audio Transcriber

## Purpose

This audio transcriber built on IBM's [watson speech to text](https://www.ibm.com/watson/services/speech-to-text/) service automatically transcribes audio files added to a specified folder

## Setup

#### Python Installation

This application requires python 3 and pip. tkinter is necessary if you want to use the gui for settings, but it is not required. On Mac and Windows, the installer at https://www.python.org/ includes tkinter and pip by default. On Linux, python 3 along with pip and tkinter may or may not be pre-installed. The packages you need are python3, python3-pip and python3-tk.

#### Dependency Installation

This product includes software originally developed by IBM Corporation
Copyright 2018 IBM Corp.

NOTICE: The watson-developer-cloud python sdk is licensed under the Apache 2.0 license.
Do not distribute it without complying with the license.

```
# In powershell/cmd/terminal, run the following
pip3 install --upgrade "watson-developer-cloud>=1.4.0"
```

#### Running the applications

There are three runnable files in the src folder. The settings_cli.py file will allow you to update your credentials and directories for speech and text files via the command line. The settings_gui.py file will allow you to update the same using a gui interface. The run.py file allows you to update the settings, then waits for files to be transcribed. It tries to launch the tkinter gui. If tkinter is not available it will fall back on the command line interface.

#### This application generates a config file for you to add your plain text credentials to, so **DO NOT** commit the config file to a public repository!!!

```
# In powershell/cmd/terminal, run the following:
python3 /path/to/file/run.py
python3 /path/to/file/settings_cli.py
python3 /path/to/file/settings_gui.py
```

## License

[MIT](https://github.com/blaubachn/transcriber/blob/master/LICENSE.md)
