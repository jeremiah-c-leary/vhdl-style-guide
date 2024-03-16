# -*- coding: utf-8 -*-
import argparse
import os
import pathlib
import subprocess
import sys
import unittest
from tempfile import TemporaryFile
from unittest import mock

from tests import utils
from vsg import cmd_line_args, version

sAFile = os.path.join(os.path.dirname(__file__),'a.vhd')
sBFile = os.path.join(os.path.dirname(__file__),'b.vhd')
sMissingFile = os.path.join(os.path.dirname(__file__),'missing.vhd')
sGlobFile = os.path.join(os.path.dirname(__file__),'*.vhd')
sInvalidGlobFile = os.path.join(os.path.dirname(__file__),'*.vhs')


class test(unittest.TestCase):

    def test_filename_w_single_file(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sAFile])

        lExpected = [sAFile]
        lExpected.sort()

        oActual = cmd_line_args.parse_command_line_arguments()
        lActual = oActual.filename
        lActual.sort()

        self.assertEqual(lActual, lExpected)

    def test_filename_w_two_files(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sAFile, sBFile])

        lExpected = [sAFile, sBFile]
        lExpected.sort()

        oActual = cmd_line_args.parse_command_line_arguments()
        lActual = oActual.filename
        lActual.sort()

        self.assertEqual(lActual, lExpected)

    def test_filename_w_two_files_positional(self):
        sys.argv = ['vsg']
        sys.argv.extend([sAFile, sBFile])

        lExpected = [sAFile, sBFile]
        lExpected.sort()

        oActual = cmd_line_args.parse_command_line_arguments()
        lActual = oActual.filename
        lActual.sort()

        self.assertEqual(lActual, lExpected)

    def test_filename_w_two_files_positional_merge(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sAFile, sBFile])

        lExpected = [sAFile, sBFile]
        lExpected.sort()

        oActual = cmd_line_args.parse_command_line_arguments()
        lActual = oActual.filename
        lActual.sort()

        self.assertEqual(lActual, lExpected)

    def test_valid_glob(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sGlobFile])

        lExpected = [sAFile, sBFile]
        lExpected.sort()

        oActual = cmd_line_args.parse_command_line_arguments()
        lActual = oActual.filename
        lActual.sort()

        self.assertEqual(lActual, lExpected)

    def test_valid_glob_w_individual_files(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sGlobFile, sAFile, sGlobFile, sBFile])

        lExpected = [sAFile, sBFile, sAFile, sAFile, sBFile, sBFile]
        lExpected.sort()

        oActual = cmd_line_args.parse_command_line_arguments()
        lActual = oActual.filename
        lActual.sort()

        self.assertEqual(lActual, lExpected)

