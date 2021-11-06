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
    def test_group(self, mock_stdout):

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
