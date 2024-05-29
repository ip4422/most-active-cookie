import argparse
from app_logger import AppLogger

HEADERS = ['cookie', 'timestamp']


class CookieLogProcessor:
    def __init__(self, filename, log_level=None, logger=None):
        self.filename = filename
        self._filtered_cookies = {}
        if logger is None:
            log_config = AppLogger(name=__name__, log_level=log_level)
            self.logger = log_config.logger
        else:
            self.logger = logger
        self.logger.info(
            f'Initialized CookieLogProcessor with file: {self.filename}')

    def read_log_file(self):
        self.logger.info(f'Reading log file: {self.filename}')
        self.cookeis = []

        with open(self.filename, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    self.cookie_log_header = line.strip().split(',')
                    if len(self.cookie_log_header) != len(HEADERS):
                        raise ValueError(
                            'Wrong log file format. Header columns do not match the expected format. Header format should be string: cookie,timestamp')
                    for i, header_column in enumerate(HEADERS):
                        if header_column != self.cookie_log_header[i]:
                            raise ValueError(
                                f'Wrong log file format. Header column \'{header_column}\' not found in the file. Header format should be string: cookie,timestamp')
                else:
                    cookie_line = line.strip()
                    if cookie_line:
                        self.cookeis.append(cookie_line.split(','))

        if len(self.cookeis) == 0:
            raise ValueError('No cookies found in the log file')
        self.logger.info(
            f'Read {len(self.cookeis)} cookies from file')

    def __filter_and_count_cookies(self, target_date):
        self.logger.info(
            f'Filtering and counting cookies for date: {target_date}')
        for line in self.cookeis:
            cookie, timestamp = line
            if target_date in timestamp:
                self._filtered_cookies[cookie] = self._filtered_cookies.get(
                    cookie, 0) + 1
        self.logger.info(f'Counted cookies: {dict(self._filtered_cookies)}')

    def find_most_active_cookies(self, target_date):
        self.__filter_and_count_cookies(target_date)
        if not self._filtered_cookies:
            self.logger.info('No cookies found for the given date')
            return []
        max_count = max(self._filtered_cookies.values())
        most_active = [cookie for cookie,
                       count in self._filtered_cookies.items() if count == max_count]
        self.logger.info(f'Most active cookies: {most_active}')
        return most_active


class CookieLogCLI:
    def __init__(self, logger=None):
        self.logger = logger
        self.parser = argparse.ArgumentParser(
            description='Find the most active cookie in a log file for a specific day.')
        self.parser.add_argument(
            '-f', '--file', required=True, help='Path to the cookie log file')
        self.parser.add_argument('-d', '--date', required=True,
                                 help='Date (YYYY-MM-DD) to find the most active cookie')
        self.parser.add_argument('--log-level', type=str, default='NOTSET',
                                 choices=['NOTSET', 'DEBUG', 'INFO',
                                          'WARNING', 'ERROR', 'CRITICAL'],
                                 help='Set the logging level. By default, logging is disabled')
        self.parser.add_argument('--log-file', type=str,
                                 help='Optional log file name. By default, logging is disabled')

    def parse_arguments(self):
        self.args = self.parser.parse_args()
        self.file = self.args.file
        self.date = self.args.date
        self.log_level = self.args.log_level
        self.log_file = self.args.log_file

        if self.logger is None:
            local_log_config = AppLogger(
                name=__name__, log_to_file=True if self.log_file else False,
                file_name=self.log_file, log_level=self.log_level)
            self.logger = local_log_config.logger

        arguments_string = ', '.join(
            f"{key}='{value}'" for key, value in vars(self.args).items())
        self.logger.info("Provided cli arguments: %s", arguments_string)

    def run(self):
        try:
            processor = CookieLogProcessor(
                self.file, self.log_level, self.logger)
            processor.read_log_file()
            most_active_cookies = processor.find_most_active_cookies(
                self.date)

            for cookie in most_active_cookies:
                print(cookie)
        except Exception as e:
            self.logger.error("An error occurred: %s", e)


if __name__ == "__main__":
    cli = CookieLogCLI()
    cli.parse_arguments()
    cli.run()
