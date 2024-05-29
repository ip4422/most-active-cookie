import logging
DEFAULT_LOG_FILE = 'most_active_cookie.log'


class AppLogger:
    def __init__(self, name=__name__, log_to_file=False,
                 file_name=DEFAULT_LOG_FILE, log_level=logging.NOTSET):
        self.logger = logging.getLogger(name)
        if log_level == None:
            self.logger.setLevel(logging.NOTSET)
        else:
            self.logger.setLevel(log_level)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        if not self.logger.hasHandlers():
            if log_to_file:
                file_handler = logging.FileHandler(file_name)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def set_log_level(self, log_level):
        self.logger.setLevel(log_level)
