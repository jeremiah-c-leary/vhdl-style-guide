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

    @unittest.skipIf(os.getenv("SKIP_TEST_ON_GITHUB") == "True", reason="GitHub may not have file available")
    @unittest.skipIf(utils.is_windows(), "The command 'file' does not exist on Windows.")
    @mock.patch("sys.stdout")
    def test_utf_8(self, mock_stdout):
        # copy test file
        shutil.copy(os.path.join("tests", "vsg", "file_encodings", "utf-8_encoded.vhd"), os.path.join(self._tmpdir.name, "utf-8_encoded.vhd"))
        # check encoding before fixing
        result = subprocess.run(["file", os.path.join(self._tmpdir.name, "utf-8_encoded.vhd")], capture_output=True, text=True)

        self.assertTrue("UTF-8 Unicode text" in result.stdout)

        sys.argv = ["vsg", "--fix", "-f", os.path.join(self._tmpdir.name, "utf-8_encoded.vhd"), "-p 1"]

        try:
            __main__.main()
        except SystemExit:
            pass

        # check encoding before fixing
        result = subprocess.run(["file", os.path.join(self._tmpdir.name, "utf-8_encoded.vhd")], capture_output=True, text=True)

        self.assertTrue("UTF-8 Unicode text" in result.stdout)

    @unittest.skipIf(os.getenv("SKIP_TEST_ON_GITHUB") == "True", reason="GitHub may not have file available")
    @unittest.skipIf(utils.is_windows(), "The command 'file' does not exist on Windows.")
    @mock.patch("sys.stdout")
    def test_iso_8859_1(self, mock_stdout):
        # copy test file
        shutil.copy(os.path.join("tests", "vsg", "file_encodings", "iso-8859-1_encoded.vhd"), os.path.join(self._tmpdir.name, "iso-8859-1_encoded.vhd"))
        # check encoding before fixing
        result = subprocess.run(["file", os.path.join(self._tmpdir.name, "iso-8859-1_encoded.vhd")], capture_output=True, text=True)
        self.assertTrue("ISO-8859 text" in result.stdout)

        sys.argv = ["vsg", "--fix", "-f", os.path.join(self._tmpdir.name, "iso-8859-1_encoded.vhd"), "-p 1"]

        try:
            __main__.main()
        except SystemExit:
            pass

        # check encoding after fixing
        result = subprocess.run(["file", os.path.join(self._tmpdir.name, "iso-8859-1_encoded.vhd")], capture_output=True, text=True)
        self.assertTrue("ISO-8859 text" in result.stdout)
