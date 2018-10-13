from logger import Logger
from configuration_manager import Configuration_Manager
from server_should_run import ServerShouldRun
from file_manager import File_Manager
from transcriber import Transcriber
import menu
from time import sleep
from os.path import join, dirname, realpath

def run(config_manager, logger):

    logger.msg('loading configuration file...')
    config = config_manager.get_config()

    logger.msg('ensuring that file directories exist...')
    file_manager = File_Manager(config['speech'], config['text'])
    if (not file_manager.directories_exist()):
        logger.err('Please check the directories entered into the config file: ' + config_file_name)
        return

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
if __name__ == '__main__':

    # Get the configuration file
    config_file_name =  join(dirname(realpath(__file__)), '..', 'config.ini')
    configuration_manager = Configuration_Manager(config_file_name)

    # Allow the user to edit the config file and decide whether to run
    server_should_run = ServerShouldRun(False)
    menu.run(configuration_manager, server_should_run)

    if server_should_run.ask():
        logger = Logger(
            join(dirname(realpath(__file__)), '..', 'messages.log'), 
            join(dirname(realpath(__file__)), '..', 'errors.log')
        )
        try:
            run(configuration_manager, logger)
        except Exception as e:
            logger.err(str(e))
            logger.err('Please ensure that the credentials in config.ini are correct and that this machine is connected to the internet')
