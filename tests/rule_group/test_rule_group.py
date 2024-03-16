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

import contextlib
from io import StringIO

from tempfile import TemporaryDirectory

from tests import utils
from vsg import version
from vsg import __main__


def full_source_path():
    return full_file_path('test_input.vhd')

def full_fixed_path(sName):
    return full_file_path('test_input.' + sName + '.fixed.vhd')

def full_config_path(sName):
    return full_file_path(sName + '.yaml')

def full_file_path(sName):
    sTestPath = 'tests/rule_group/'
    return sTestPath + '/' + sName


class command_line_args():
    ''' This is used as an input into the version command.'''
    def __init__(self, version=False):
        self.version = version


class testMain(unittest.TestCase):
    def full_actual_path(self, sName):
        return os.path.join(self._tmpdir.name, 'test_input.' + sName + '.actual.vhd')

    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_config_1(self):

        sConfigName = 'config_1'
        shutil.copy(full_source_path(), self.full_actual_path(sConfigName))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', full_config_path(sConfigName)])
        sys.argv.extend(['-p 1'])
        sys.argv.extend(['-f', self.full_actual_path(sConfigName)])
        sys.argv.extend(['--fix'])

        try:
            __main__.main()
        except SystemExit:
            pass

        lExpected = []
        utils.read_file(full_fixed_path(sConfigName), lExpected, False)
        lActual = []
        utils.read_file(self.full_actual_path(sConfigName), lActual, False)

        self.assertEqual(lExpected, lActual)

    def test_config_2(self):

        sConfigName = 'config_2'
        shutil.copy(full_source_path(), self.full_actual_path(sConfigName))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', full_config_path(sConfigName)])
        sys.argv.extend(['-p 1'])
        sys.argv.extend(['-f', self.full_actual_path(sConfigName)])
        sys.argv.extend(['--fix'])

        try:
            __main__.main()
        except SystemExit:
            pass

        lExpected = []
        utils.read_file(full_fixed_path(sConfigName), lExpected, False)
        lActual = []
        utils.read_file(self.full_actual_path(sConfigName), lActual, False)

        self.assertEqual(lExpected, lActual)

    def test_config_3(self):

        sConfigName = 'config_3'
        shutil.copy(full_source_path(), self.full_actual_path(sConfigName))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', full_config_path(sConfigName)])
        sys.argv.extend(['-p 1'])
        sys.argv.extend(['-f', self.full_actual_path(sConfigName)])
        sys.argv.extend(['--fix'])

        try:
            __main__.main()
        except SystemExit:
            pass

        lExpected = []
        utils.read_file(full_fixed_path(sConfigName), lExpected, False)
        lActual = []
        utils.read_file(self.full_actual_path(sConfigName), lActual, False)

        self.assertEqual(lExpected, lActual)
