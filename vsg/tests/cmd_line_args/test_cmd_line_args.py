import argparse
import pathlib
import unittest
from unittest import mock
import subprocess
import os
import sys

from tempfile import TemporaryFile

from vsg.tests import utils
from vsg import version

from vsg import cmd_line_args

sAFile = os.path.join(os.path.dirname(__file__),'a.vhd')
sBFile = os.path.join(os.path.dirname(__file__),'b.vhd')
sMissingFile = os.path.join(os.path.dirname(__file__),'missing.vhd')
sGlobFile = os.path.join(os.path.dirname(__file__),'*.vhd')
sInvalidGlobFile = os.path.join(os.path.dirname(__file__),'*.vhs')


class test(unittest.TestCase):

    def test_filename_w_single_file(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sAFile])

        oActual = cmd_line_args.parse_command_line_arguments()
        self.assertEqual(oActual.filename, [sAFile])

    def test_filename_w_two_files(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sAFile, sBFile])

        oActual = cmd_line_args.parse_command_line_arguments()
        self.assertEqual(oActual.filename, [sAFile, sBFile])

    def test_valid_glob(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sGlobFile])

        oActual = cmd_line_args.parse_command_line_arguments()
        self.assertEqual(oActual.filename, [sAFile, sBFile])

    def test_valid_glob_w_individual_files(self):
        sys.argv = ['vsg']
        sys.argv.extend(['-f', sGlobFile, sAFile, sGlobFile, sBFile])

        oActual = cmd_line_args.parse_command_line_arguments()
        self.assertEqual(oActual.filename, [sAFile, sBFile, sAFile, sAFile, sBFile, sBFile])

