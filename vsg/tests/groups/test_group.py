import filecmp
import pathlib
import unittest
from unittest import mock
import os
import subprocess
import shutil
import sys
import shutil

import contextlib
from io import StringIO

from tempfile import TemporaryFile

from vsg.tests import utils
from vsg import version
from vsg import __main__


class command_line_args():
    ''' This is used as an input into the version command.'''
    def __init__(self, version=False):
        self.version = version


class testGroup(unittest.TestCase):

    @mock.patch('sys.stdout')
    def test_group_by_disabling(self, mock_stdout):

        lExpected = []

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-f', 'vsg/tests/groups/group_config_example.vhd'])
        sys.argv.extend(['-c', 'vsg/tests/groups/disable_indent_group.yaml'])
        sys.argv.extend(['-p 1'])

        with self.assertRaises(SystemExit) as cm:
            __main__.main()

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertEqual(cm.exception.code, 0)

    @mock.patch('sys.stdout')
    def test_group_with_warning_severity(self, mock_stdout):

        sOutput = ''
        sOutput += 'WARNING: vsg/tests/groups/group_config_example.vhd(2)architecture_001 -- Indent level 0\n'
        sOutput += 'WARNING: vsg/tests/groups/group_config_example.vhd(4)architecture_007 -- Indent level 0\n'
        sOutput += 'WARNING: vsg/tests/groups/group_config_example.vhd(6)architecture_008 -- Indent level 0'

        lExpected = []
        lExpected.append(mock.call(sOutput))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-f', 'vsg/tests/groups/group_config_example.vhd'])
        sys.argv.extend(['-c', 'vsg/tests/groups/warning_indent_group.yaml'])
        sys.argv.extend(['-p 1'])

        with self.assertRaises(SystemExit) as cm:
            __main__.main()

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertEqual(cm.exception.code, 0)
