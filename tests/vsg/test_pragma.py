# -*- coding: utf-8 -*-
import filecmp
import pathlib
import unittest
from unittest import mock
import os
import subprocess
import shutil
import sys
import shutil
import yaml

import contextlib
from io import StringIO

from tempfile import TemporaryFile

from tests import utils
from vsg import version
from vsg import __main__


class testMain(unittest.TestCase):

    @mock.patch('sys.stdout')
    def test_default_pragmas(self, mock_stdout):

        sCall = ''
        sCall += 'ERROR: tests/vsg/pragmas/pragmas.vhd(3)pragma_401 -- Remove blank lines below'
        sCall += '\n'
        sCall += 'ERROR: tests/vsg/pragmas/pragmas.vhd(11)pragma_401 -- Remove blank lines below'

        lExpected = []
        lExpected.append(mock.call(sCall))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['-f', 'tests/vsg/pragmas/pragmas.vhd'])
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_configuring_pragmas(self, mock_stdout):

        sCall = ''
        sCall += 'ERROR: tests/vsg/pragmas/pragmas.vhd(2)pragma_300 -- Indent level 0'
        sCall += '\n'
        sCall += 'ERROR: tests/vsg/pragmas/pragmas.vhd(9)comment_010 -- Use 2 spaces for indent'
        sCall += '\n'
        sCall += 'ERROR: tests/vsg/pragmas/pragmas.vhd(10)pragma_300 -- Use 2 spaces for indent'

        lExpected = []
        lExpected.append(mock.call(sCall))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--configuration', 'tests/vsg/pragmas/config_pragma.json'])
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)
