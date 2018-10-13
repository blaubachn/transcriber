import datetime

class ValidatedResponse:
    def __init__(self, menu_text, responses):
        self.menu_text = menu_text
        self.responses = responses
    def get(self):
        menu_selection = input(self.menu_text)
        while menu_selection not in self.responses:
            menu_selection = input(self.menu_text)
        return menu_selection

menu_message = '''
This product includes software originally developed by IBM Corporation
Copyright '''  + str(datetime.datetime.now().year) +  ''' IBM Corp.

Settings can also be updated by manually editing the file: config.ini

WARNING!!!
Be aware that ALL information entered here will be stored in 
PLAIN TEXT in an .ini config file. Please take measures to ensure 
that this file is not committed to any public repositories.
'''

menu_prompt = '''
What would you like to do? (Select A Number)
1. Update Username (See warning above)
2. Update Password (See warning above)
3. Update Speech Directory to scan for audio
4. Update Text Directory to place transcriptions
5. Exit configuration and start the transcriber
6. Exit the configuration and the transcriber

'''

menu_responses = ['1','2','3','4','5','6']

def run(config_manager, server_should_run):
    print(menu_message)
    validated_response = ValidatedResponse(menu_prompt, menu_responses)

    config_manager.print_config()
    response = validated_response.get()
    
    while True:
        if response == '1':
            config_manager.update_username(input('New Username: '))
        elif response == '2':
            config_manager.update_password(input('New Password: '))
        elif response == '3':
            config_manager.update_speech_directory(input('New Speech Directory: '))
        elif response == '4':
            config_manager.update_text_directory(input('New Text Directory: '))
        elif response == '5':
            server_should_run.allow()
            return
        elif response == '6':
            server_should_run.prevent()
            return
        
        config_manager.print_config()
        response = validated_response.get()


