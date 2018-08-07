from datetime import datetime

class Logger:
    def __init__(self, msg_file_name, err_file_name):
        self.msg_file_name = msg_file_name
        self.err_file_name = err_file_name

    def log(self, file, message):
        current_time = str(datetime.now())
        with open(file, 'a') as text_file:
            text_file.write(current_time[:current_time.rfind('.')] + ': ' + message + '\n')
            print(message)

    def msg(self, message):
        self.log(self.msg_file_name, message)
        
    def err(self, message):
        self.log(self.err_file_name, message)