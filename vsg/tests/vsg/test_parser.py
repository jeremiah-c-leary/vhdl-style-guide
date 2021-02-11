import sys
import unittest

from vsg import __main__


class TestParser(unittest.TestCase):
    def test_jobs_valid_1(self):
        sys.argv[1:] = ["-p", "3"]

        result = __main__.parse_command_line_arguments()

        self.assertEqual(result.jobs, 3)

    def test_jobs_valid_2(self):
        sys.argv[1:] = ["--jobs", "1"]

        result = __main__.parse_command_line_arguments()

        self.assertEqual(result.jobs, 1)

    def test_jobs_invalid_1(self):
        sys.argv[1:] = ["-p", "-3"]

        with self.assertRaises(SystemExit) as cm:
            __main__.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 2)

    def test_jobs_invalid_2(self):
        sys.argv[1:] = ["--jobs", "0"]

        with self.assertRaises(SystemExit) as cm:
            __main__.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 2)

    def test_jobs_invalid_3(self):
        sys.argv[1:] = ["--jobs", "3.5"]

        with self.assertRaises(SystemExit) as cm:
            __main__.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 2)

    def test_jobs_invalid_4(self):
        sys.argv[1:] = ["--jobs", "notanumber"]

        with self.assertRaises(SystemExit) as cm:
            __main__.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 2)
