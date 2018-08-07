from logger import Logger
from configuration_manager import Configuration_Manager
from file_manager import File_Manager
from transcriber import Transcriber
from time import sleep
from os.path import join, dirname, realpath

config_file_name =  join(dirname(realpath(__file__)), '..', 'config.ini')
msg_log_file_name = join(dirname(realpath(__file__)), '..', 'messages.log')
err_log_file_name = join(dirname(realpath(__file__)), '..', 'errors.log')

logger = Logger(msg_log_file_name, err_log_file_name)

def run():
    #----------------------------------------------------------------------
    # Load the configuration file
    #----------------------------------------------------------------------
    logger.msg('loading configuration file...')
    config_file = Configuration_Manager(config_file_name)
    if (not config_file.exists()):
        logger.err('Please set up the application settings in ' + config_file_name + ' by opening it or running configure')
        config_file.set_config('<username>', '<password>', '<path/to/speech/files>', '<path/to/text/files>')
        return
    config = config_file.get_config()
    logger.msg('configuration file loaded')

    #----------------------------------------------------------------------
    # Ensure that the directories exist
    #----------------------------------------------------------------------
    logger.msg('ensuring that file directories exist...')
    file_manager = File_Manager(config['speech'], config['text'])
    if (not file_manager.directories_exist()):
        logger.err('Please check the directories entered into the config file: ' + config_file_name)
        return
    logger.msg('file directories exist')

    #----------------------------------------------------------------------
    # Transcribe the files
    #----------------------------------------------------------------------
    logger.msg('waiting for files to transcribe...')
    transcriber = Transcriber(config['username'], config['password'], file_manager) # Create transcription object
    while(True):                                                                    # Loop for eternity
        for file in file_manager.speech_files_without_text_files():                 # Loop through files that need to be transcribed
            logger.msg('Transcribing: ' + file + '...')
            transcriber.transcribe(file)                                            # Transcribe the current file
            logger.msg(file + ' transcribed')
            logger.msg('waiting for files to transcribe...')
        sleep(10)                                                                   # Wait for 10 seconds

#--------------------------------------------------------------------------
# Run the settings application
#--------------------------------------------------------------------------
try:
    import settings_gui
    settings_gui.run(config_file_name)
except:
    import settings_cli
    settings_cli.run(config_file_name)

#--------------------------------------------------------------------------
# Run the application, and log an error if it breaks
# TODO: Give specific errors from watson issues.
#--------------------------------------------------------------------------
try:
    run()
except Exception as e:
    logger.err(str(e))
    logger.err('Please ensure that the credentials in config.ini are correct and that this machine is connected to the internet')
