# -*- coding: utf-8 -*-
import sys
import unittest
from unittest.mock import MagicMock, patch
import argparse

from vsg import cmd_line_args


class TestParser(unittest.TestCase):
    def test_jobs_valid_1(self):
        sys.argv[1:] = ["-p", "3"]

        result = cmd_line_args.parse_command_line_arguments()

        self.assertEqual(result.jobs, 3)

    def test_jobs_valid_2(self):
        sys.argv[1:] = ["--jobs", "1"]

        result = cmd_line_args.parse_command_line_arguments()

        self.assertEqual(result.jobs, 1)

    def test_jobs_invalid_1(self):
        argparse_mock = unittest.mock.MagicMock()
        sys.argv[1:] = ["-p", "-3"]

        with patch('argparse.ArgumentParser._print_message', argparse_mock):
            with self.assertRaises(SystemExit) as cm:
                result = cmd_line_args.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 1)

    def test_jobs_invalid_2(self):
        argparse_mock = unittest.mock.MagicMock()
        sys.argv[1:] = ["--jobs", "0"]

        with patch('argparse.ArgumentParser._print_message', argparse_mock):
            with self.assertRaises(SystemExit) as cm:
                cmd_line_args.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 1)

    def test_jobs_invalid_3(self):
        argparse_mock = unittest.mock.MagicMock()
        sys.argv[1:] = ["--jobs", "3.5"]

        with patch('argparse.ArgumentParser._print_message', argparse_mock):
            with self.assertRaises(SystemExit) as cm:
                cmd_line_args.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 1)

    def test_jobs_invalid_4(self):
        argparse_mock = unittest.mock.MagicMock()
        sys.argv[1:] = ["--jobs", "notanumber"]

        with patch('argparse.ArgumentParser._print_message', argparse_mock):
            with self.assertRaises(SystemExit) as cm:
                cmd_line_args.parse_command_line_arguments()

        self.assertEqual(cm.exception.code, 1)
