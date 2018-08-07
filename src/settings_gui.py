from tkinter import *
from tkinter import filedialog
from configuration_manager import Configuration_Manager
import webbrowser
import datetime
from os.path import join, dirname, realpath

settings_message = '''
Hi! Welcome to the audio transcriber.

This application will:
- Scan a folder (Speech Directory) every few seconds 
- Transcribe any new files that you add to it.
- Create transcription files in a folder (Text Directory)

Here, you can enter:
- Your credentials for your IBM cloud account
- The folder to scan for speech files
- The folder to place the text files

If you don't have an IBMid set up for Speech to Text,
please do so at:
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

def run(config_file_location):
    config_file = Configuration_Manager(config_file_location)

    window = Tk()
    window.wm_title('Settings')

    label_width = 30
    textb_width = 50
    total_width = label_width + textb_width

    #-------------------------------------------------------------------------------
    # Text Boxes
    #-------------------------------------------------------------------------------
    message_label = Label(window, width=total_width, justify = LEFT, text=settings_message)

    def stt_link(event):
        webbrowser.open_new(r'https://www.ibm.com/watson/services/speech-to-text/')
    link_label = Label(window, text='Watson Speech To Text', fg='blue', cursor='hand2')
    link_label.bind('<Button-1>', stt_link)

    warning_label = Label(window, width=total_width, fg='red', text=settings_warning)
    copyright_label = Label(window, width=total_width, text=settings_copyright)

    username_label = Label(window, width=label_width, text='Username')
    username_string = StringVar()
    username_entry = Entry(window, width=textb_width, textvariable = username_string)

    password_label = Label(window, width=label_width, text='Password')
    password_string = StringVar()
    password_entry = Entry(window, width=textb_width, textvariable = password_string)

    speech_string = StringVar()
    speech_entry = Entry(window, width=textb_width, textvariable = speech_string)
    
    text_string = StringVar()
    text_entry = Entry(window, width=textb_width, textvariable = text_string)

    def set_entry(entry, text):
        entry.delete(0, END)
        entry.insert(END, text)

    if (config_file.exists()):
        config = config_file.get_config()
        set_entry(username_entry, config['username'])
        set_entry(password_entry, config['password'])
        set_entry(speech_entry,   config['speech'])
        set_entry(text_entry,     config['text'])

    #-------------------------------------------------------------------------------
    # Button Handlers
    #-------------------------------------------------------------------------------
    def choose_speech_directory():
        set_entry(speech_entry, filedialog.askdirectory())
        
    def choose_text_directory():
        set_entry(text_entry, filedialog.askdirectory())

    def save_config():
        config_file.set_config(username_string.get(), password_string.get(), speech_string.get(), text_string.get())
        window.destroy()
        
    #-------------------------------------------------------------------------------
    # Buttons
    #-------------------------------------------------------------------------------
    select_speech_dir = Button(   window, width = label_width, text = 'Choose Speech Directory', command = choose_speech_directory)
    select_text_dir = Button(     window, width = label_width, text = 'Choose Text Directory',   command = choose_text_directory)
    cancel = Button(              window, width = label_width, text = 'Cancel',                  command = window.destroy, fg = 'red')
    save = Button(                window, width = textb_width, text = 'Save',                    command = save_config,    fg = 'green' )

    #-------------------------------------------------------------------------------
    # UI Placement
    #-------------------------------------------------------------------------------
    message_label.grid(     column = 0, row = 0, columnspan = 2)
    link_label.grid(        column = 0, row = 1, columnspan = 2)
    warning_label.grid(     column = 0, row = 2, columnspan = 2)

    username_label.grid(    column = 0, row = 3)
    password_label.grid(    column = 0, row = 4)
    select_speech_dir.grid( column = 0, row = 5)
    select_text_dir.grid(   column = 0, row = 6)
    cancel.grid(            column = 0, row = 7)

    username_entry.grid(    column = 1, row = 3)
    password_entry.grid(    column = 1, row = 4)
    speech_entry.grid(      column = 1, row = 5)
    text_entry.grid(        column = 1, row = 6)
    save.grid(              column = 1, row = 7)

    copyright_label.grid(   column = 0, row = 8, columnspan = 2)

    window.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    run(join(dirname(realpath(__file__)), '..', 'config.ini'))
