# -*- coding: utf-8 -*-
import os
import pathlib
import shutil
import sys
import unittest
from tempfile import TemporaryDirectory
from unittest import mock

from vsg import __main__


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

    def check_file_encoding(self, file_path, expected_encoding):
        """
        Check a file is decodable using the encoding specified
        """
        file_path = pathlib.Path(file_path).resolve()
        with open(file_path, "rb") as f:
            raw_data = f.read(8192)
            try:
                raw_data.decode(expected_encoding, errors="strict")
            except UnicodeDecodeError as ude:
                raise AssertionError(f"File {file_path} is not decodable using encoding {expected_encoding}") from ude

    @mock.patch("sys.stdout")
    def test_utf_8(self, mock_stdout):
        test_file = os.path.join(self._tmpdir.name, "utf-8_encoded.vhd")
        # copy test file
        shutil.copy(os.path.join("tests", "vsg", "file_encodings", "utf-8_encoded.vhd"), test_file)
        # check encoding before fixing
        self.check_file_encoding(test_file, "utf-8")

        sys.argv = ["vsg", "--fix", "-f", test_file, "-p 1"]

        try:
            __main__.main()
        except SystemExit:
            pass

        # check encoding after fixing
        self.check_file_encoding(test_file, "utf-8")

    @mock.patch("sys.stdout")
    def test_iso_8859_1(self, mock_stdout):
        # copy test file
        test_file = os.path.join(self._tmpdir.name, "iso-8859-1_encoded.vhd")
        shutil.copy(os.path.join("tests", "vsg", "file_encodings", "iso-8859-1_encoded.vhd"), test_file)
        # check encoding before fixing
        self.check_file_encoding(test_file, "iso-8859-1")

        sys.argv = ["vsg", "--fix", "-f", test_file, "-p 1"]

        try:
            __main__.main()
        except SystemExit:
            pass

        # check encoding after fixing
        self.check_file_encoding(test_file, "iso-8859-1")

    def test_encoding_check(self):
        iso8859_test_file = os.path.join("tests", "vsg", "file_encodings", "iso-8859-1_encoded.vhd")
        utf8_test_file = os.path.join("tests", "vsg", "file_encodings", "utf-8_encoded.vhd")
        # make sure encoding check fails on the wrong encoding
        try:
            self.check_file_encoding(iso8859_test_file, "utf-8")
            self.fail("File should not be decodable using encoding 'utf-8' check_file_encoding is not working as expected")
        except AssertionError:
            pass
        try:
            self.check_file_encoding(utf8_test_file, "iso-8859-1")
            self.fail("File should not be decodable using encoding 'iso-8859-1' check_file_encoding is not working as expected")
        except AssertionError:
            pass
