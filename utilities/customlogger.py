import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        log_directory = "Logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_file_path = os.path.join(log_directory,"automatic.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p')

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger