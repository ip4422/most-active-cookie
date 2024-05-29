import unittest
from io import StringIO
import os
import logging
from contextlib import redirect_stdout
from unittest.mock import patch
from most_active_cookie import CookieLogProcessor, CookieLogCLI

TEST_COOKIE_LOG = 'test_cookie_log.csv'


# Configure logging for tests
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestCookieLogProcessor(unittest.TestCase):

    def test_read_log_file(self):
        test_filename = TEST_COOKIE_LOG
        with open(test_filename, 'w') as f:
            f.write("cookie,timestamp\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n")

        processor = CookieLogProcessor(test_filename)
        processor.read_log_file()
        self.assertEqual(len(processor.cookeis), 2)
        self.assertEqual(
            processor.cookeis[1], ["SAZuXPGUrfbcn5UA", "2018-12-09T10:13:00+00:00"])

        os.remove(test_filename)

    def test_find_most_active_cookies_single(self):
        test_filename = TEST_COOKIE_LOG
        with open(test_filename, 'w') as f:
            f.write("cookie,timestamp\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n")
            f.write("5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:20:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:21:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n")
            f.write("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n")

        processor = CookieLogProcessor(test_filename)
        processor.read_log_file()
        most_active_cookies = processor.find_most_active_cookies('2018-12-09')
        self.assertEqual(most_active_cookies, ['SAZuXPGUrfbcn5UA'])

        os.remove(test_filename)

    def test_find_most_active_cookies_multiple(self):
        test_filename = TEST_COOKIE_LOG
        with open(test_filename, 'w') as f:
            f.write("cookie,timestamp\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n")
            f.write("5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:21:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n")
            f.write("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n")

        processor = CookieLogProcessor(test_filename)
        processor.read_log_file()
        most_active_cookies = processor.find_most_active_cookies('2018-12-09')
        self.assertEqual(sorted(most_active_cookies), sorted(
            ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA']))

        os.remove(test_filename)


class TestCookieLogCLI(unittest.TestCase):
    def test_main(self):
        test_filename = TEST_COOKIE_LOG
        with open(test_filename, 'w') as f:
            f.write("cookie,timestamp\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n")
            f.write("5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00\n")
            f.write("AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n")
            f.write("SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n")
            f.write("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n")

        test_args = ['most_active_cookie_class.py',
                     '-f', test_filename, '-d', '2018-12-09']
        with patch('sys.argv', test_args):
            f = StringIO()
            with redirect_stdout(f):
                cli = CookieLogCLI()
                cli.parse_arguments()
                cli.run()
            output = f.getvalue().strip().split('\n')

        self.assertIn('AtY0laUfhglK3lC7', output)

        os.remove(test_filename)


if __name__ == '__main__':
    unittest.main()
