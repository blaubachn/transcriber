from configuration_manager import Configuration_Manager
import datetime
from os.path import join, dirname, realpath

settings_message = '''
Hi! Welcome to the audio transcriber.
If you aren't super comfortable with the command line
(Or would rather use a file chooser gui)
You can install tkinter to use the gui instead.

This application will:
- Scan a folder (Speech Directory) every few seconds 
- Transcribe any new files that you add to it.
- Create transcription files in a folder (Text Directory)

Here, you can enter:
- Your credentials for your IBM cloud account
- The folder to scan for speech files
- The folder to place the text files
'''

settings_warning = '''
WARNING!!!

Be aware that ALL information entered here will be stored in 
PLAIN TEXT in an .ini config file. Please take measures to ensure 
that this file is not committed to any public repositories.
'''

settings_copyright = '''
This product includes software originally developed by IBM Corporation
Copyright ''' + str(datetime.datetime.now().year) + ''' IBM Corp.
'''

settings_menu = '''
What would you like to do? (Select A Number)
1. Change Username
2. Change Password
3. Change Speech Directory
4. Change Text Directory
5. Exit configuration

'''

def run(config_file_location):
    print(settings_message + settings_warning + settings_copyright)

    config_file = Configuration_Manager(config_file_location)

    config_file.print_config()
    action = input(settings_menu)
    
    while(action != '5'):

        if action == '1':
            config_file.update_username(input('New Username: '))
        elif action == '2':
            config_file.update_password(input('New Password: '))
        elif action == '3':
            config_file.update_speech_directory(input('New Speech Directory: '))
        elif action == '4':
            config_file.update_text_directory(input('New Text Directory: '))
        else:
            print('Oops! I only have 5 options so far. There will probably be more in the future, but for now there are only 5')
        
        config_file.print_config()
        action = input(settings_menu)
    print('Yay! you did it! :)')


if __name__ == "__main__":
    # execute only if run as a script
    run(join(dirname(realpath(__file__)), '..', 'config.ini'))
