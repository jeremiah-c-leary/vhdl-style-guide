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
from tempfile import TemporaryFile
from unittest import mock

from tests import utils
from vsg import __main__, version


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version


class testGroup(unittest.TestCase):
    @mock.patch("sys.stdout")
    def test_group_by_disabling(self, mock_stdout):
        lExpected = []

        sys.argv = ["vsg"]
        sys.argv.extend(["--output_format", "syntastic"])
        sys.argv.extend(["-f", "tests/groups/group_config_example.vhd"])
        sys.argv.extend(["-c", "tests/groups/disable_indent_group.yaml"])
        sys.argv.extend(["-p 1"])

        with self.assertRaises(SystemExit) as cm:
            __main__.main()

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertEqual(cm.exception.code, 0)

    @mock.patch("sys.stdout")
    def test_group_with_warning_severity(self, mock_stdout):
        sOutput = ""
        sOutput += "WARNING: tests/groups/group_config_example.vhd(2)architecture_001 -- Indent level 0\n"
        sOutput += "WARNING: tests/groups/group_config_example.vhd(4)architecture_007 -- Indent level 0\n"
        sOutput += "WARNING: tests/groups/group_config_example.vhd(6)architecture_008 -- Indent level 0"

        lExpected = []
        lExpected.append(mock.call(sOutput))
        lExpected.append(mock.call("\n"))

        sys.argv = ["vsg"]
        sys.argv.extend(["--output_format", "syntastic"])
        sys.argv.extend(["-f", "tests/groups/group_config_example.vhd"])
        sys.argv.extend(["-c", "tests/groups/warning_indent_group.yaml"])
        sys.argv.extend(["-p 1"])

        with self.assertRaises(SystemExit) as cm:
            __main__.main()

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertEqual(cm.exception.code, 0)
