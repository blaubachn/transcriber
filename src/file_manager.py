from os.path import join, dirname, isfile, isdir
from os import listdir

class File_Manager:
    def __init__(self, speech_dir, text_dir):
        self.speech_dir = speech_dir
        self.text_dir = text_dir
    
    def directories_exist(self):
        return isdir(self.speech_dir) and isdir(self.text_dir)

    def speech_files_without_text_files(self):
        return [
            audio_file
            for audio_file in listdir(self.speech_dir)
            if audio_file + '.txt' not in listdir(self.text_dir) and audio_file[audio_file.rfind('.') + 1:] != 'txt'
            and audio_file[audio_file.rfind('.') + 1:] != 'txt'
        ]

    def speech_file_path(self, file_name):
        return join(self.speech_dir, file_name)

    def content_type(self, audio_file):
        return 'audio/' + audio_file[audio_file.rfind('.') + 1:]

    def write_transcription_to_file(self, file_name, transcript):
        with open(join(self.text_dir, file_name + '.txt'), 'w') as text_file:
            text_file.write(transcript)
