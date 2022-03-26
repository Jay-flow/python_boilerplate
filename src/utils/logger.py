from datetime import date

from src.abstracts.singleton import Singleton
from src.utils.env import get
from src.utils.funtions import create_the_directory
from src.utils.logger_colored_formatter import (LoggerColoredFormatter,
                                                formatter_message, logging)
from src.utils.path import os_path_split


class Logger(metaclass=Singleton):
    def __init__(self):
        logging.basicConfig(level=logging.NOTSET)

        self.logger = logging.getLogger()

        self.info = self.logger.info
        self.debug = self.logger.debug
        self.warning = self.logger.warning
        self.error = self.logger.error

        self.log_dir_path = get('SAVE_LOG_PATH')
        create_the_directory(self.log_dir_path)

    def set_up_log_handler(self, file_name: str) -> None:
        self.set_file_handler(file_name)
        self.set_stream_handler()

    def set_file_handler(self, file_name: str) -> None:
        file_handler = self.__set_log_file_name(file_name)
        formatter = logging.Formatter(
            '%(asctime)s[%(levelname)s] %(message)s (%(filename)s: %(lineno)s)')

        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __set_log_file_name(self, file_name: str) -> logging.FileHandler:
        log_file_name = f'{date.today()}-{file_name}.log'
        file_handler = logging.FileHandler(
            f'{self.log_dir_path}/{log_file_name}',
            encoding='utf-8'
        )

        return file_handler

    def set_stream_handler(self) -> None:
        FORMAT = "[%(levelname)s]  %(message)s ($BOLD%(filename)s$RESET: %(lineno)d)"
        color_format = formatter_message(FORMAT, True)
        color_formatter = LoggerColoredFormatter(color_format)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(color_formatter)
        self.logger.addHandler(stream_handler)

    def decorate_log(self, log_message: str) -> None:
        result_message = ""
        log_messages = log_message.split("\n")
        
        for index, message in enumerate(log_messages):
            if index == len(log_messages) - 1:
                result_message += f"# {message}"
            else:
                result_message += f"# {message}\n"

        decorate_message = f"""
#######################################################
{result_message}
#######################################################"""
        self.info(decorate_message)

    def write_file(self, file_name: str, text: str) -> None:
        with open(f"{self.log_dir_path}{os_path_split}{file_name}.log", "a") as f:
            f.write(f"{text}\n")

    def write_error_log_file(self, label: str, message: str):
        Logger().error(
            f"Record it in the {label} log file and move on."
        )
        Logger().write_file(label, message)


logger = Logger()

if __name__ == '__main__':
    logger.info('Log')
    logger.decorate_log('Decorate log')
