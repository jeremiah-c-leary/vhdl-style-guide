# -*- coding: utf-8 -*-
import os
import shutil
import sys
import unittest
from unittest import mock

from vsg import __main__


class testMain(unittest.TestCase):
    def setUp(self):
        if os.path.exists("deleteme.vhd"):
            os.remove("deleteme.vhd")

    def tearDown(self):
        if os.path.exists("deleteme.vhd"):
            os.remove("deleteme.vhd")

    @mock.patch("sys.stdout")
    def test_passing_file(self, mock_stdout):
        shutil.copy("tests/vsg/file_timestamp/passing_file.vhd", "deleteme.vhd")
        expected = os.path.getmtime("deleteme.vhd")

        sys.argv = ["vsg"]
        sys.argv.extend(["-f", "deleteme.vhd"])
        sys.argv.extend(["--output_format", "syntastic"])
        sys.argv.extend(["-p 1"])
        sys.argv.extend(["--fix"])

        try:
            __main__.main()
        except SystemExit:
            pass

        actual = os.path.getmtime("deleteme.vhd")

        self.assertEqual(actual, expected)

    @mock.patch("sys.stdout")
    def test_failing_file(self, mock_stdout):
        shutil.copy("tests/vsg/file_timestamp/failing_file.vhd", "deleteme.vhd")
        expected = os.path.getmtime("deleteme.vhd")

        sys.argv = ["vsg"]
        sys.argv.extend(["-f", "deleteme.vhd"])
        sys.argv.extend(["--output_format", "syntastic"])
        sys.argv.extend(["-p 1"])
        sys.argv.extend(["--fix"])

        try:
            __main__.main()
        except SystemExit:
            pass

        actual = os.path.getmtime("deleteme.vhd")

        self.assertNotEqual(actual, expected)
