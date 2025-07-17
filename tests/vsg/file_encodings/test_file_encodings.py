# -*- coding: utf-8 -*-
import contextlib
import filecmp
import os
import pathlib
import shutil
import subprocess
import sys
import unittest
from io import StringIO
from tempfile import TemporaryDirectory
from unittest import mock

import yaml

from tests import utils
from vsg import __main__, version


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version
        self.style = "indent_only"
        self.configuration = []
        self.debug = False
        self.fix_only = False
        self.stdin = False
        self.force_fix = False
        self.fix = False


class testMain(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    def check_file_type(self, file_path, expected_type, expected_encoding):
        """
        Check the detected mime type and encoding of a file matches the expected values.
        This uses `file --brief --mime-type` and `file --brief --mime-encoding`
        to get machine readable versions of a file's mime type and encoding.
        """
        # Use full path to executable to avoid PATH injection
        file_cmd = shutil.which("file")
        if not file_cmd:
            raise FileNotFoundError("file command not found in PATH")

        # Validate and sanitize file_path input
        file_path = pathlib.Path(file_path).resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"File does not exist: {file_path}")
        if not file_path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")
        file_path_str = str(file_path)

        try:
            mime_type = subprocess.check_output([file_cmd, "--brief", "--mime-type", file_path_str], text=True).strip()
            mime_encoding = subprocess.check_output([file_cmd, "--brief", "--mime-encoding", file_path_str], text=True).strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"file command failed: {e}") from e

        self.assertEqual(mime_type, expected_type)
        self.assertEqual(mime_encoding, expected_encoding)

    @unittest.skipIf(os.getenv("HOME") == "/home/runner", reason="GitHub may not have file available")
    @unittest.skipIf(utils.is_windows(), "The command 'file' does not exist on Windows.")
    @mock.patch("sys.stdout")
    def test_utf_8(self, mock_stdout):
        test_file = os.path.join(self._tmpdir.name, "utf-8_encoded.vhd")
        # copy test file
        shutil.copy(os.path.join("tests", "vsg", "file_encodings", "utf-8_encoded.vhd"), test_file)
        # check encoding before fixing
        self.check_file_type(test_file, "text/plain", "utf-8")

        sys.argv = ["vsg", "--fix", "-f", test_file, "-p 1"]

        try:
            __main__.main()
        except SystemExit:
            pass

        # check encoding after fixing
        self.check_file_type(test_file, "text/plain", "utf-8")

    @unittest.skipIf(os.getenv("HOME") == "/home/runner", reason="GitHub may not have file available")
    @unittest.skipIf(utils.is_windows(), "The command 'file' does not exist on Windows.")
    @mock.patch("sys.stdout")
    def test_iso_8859_1(self, mock_stdout):
        # copy test file
        test_file = os.path.join(self._tmpdir.name, "iso-8859-1_encoded.vhd")
        shutil.copy(os.path.join("tests", "vsg", "file_encodings", "iso-8859-1_encoded.vhd"), test_file)
        # check encoding before fixing
        self.check_file_type(test_file, "text/plain", "iso-8859-1")

        sys.argv = ["vsg", "--fix", "-f", test_file, "-p 1"]

        try:
            __main__.main()
        except SystemExit:
            pass

        # check encoding after fixing
        self.check_file_type(test_file, "text/plain", "iso-8859-1")
