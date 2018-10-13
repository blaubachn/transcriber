from watson_developer_cloud import SpeechToTextV1
from file_manager import File_Manager
import json

class Transcriber:
    def __init__(self, username, password, file_manager):
        self.speech_to_text = SpeechToTextV1(username = username, password = password)
        self.file_manager = file_manager

    def transcribe(self, file):
        with open(self.file_manager.speech_file_path(file), 'rb') as speech_file:
            transcript_data = self.speech_to_text.recognize(
                audio = speech_file, 
                content_type = self.file_manager.content_type(file)
            )
            transcript = "".join([result["alternatives"][0]["transcript"] for result in transcript_data.result["results"]])
            self.file_manager.write_transcription_to_file(file, transcript)
        