import os
import pathlib
import unittest
from unittest import mock
import sys
import subprocess
sys.path.append('vsg')

from vsg.rules import source_file
from vsg import vhdlFile
from vsg import __main__
from vsg.tests import utils

sNoPermissionFile = 'no_permission.vhd'
sEmptyFile = 'empty_file.vhd'

sOutputNoFile = os.path.join(os.path.dirname(__file__),'output_no_file.txt')
sOutputNoPermission = os.path.join(os.path.dirname(__file__),'output_no_permission.txt')
sOutputEmptyFile = os.path.join(os.path.dirname(__file__),'output_empty_file.txt')


class testOSError(unittest.TestCase):

    def tearDown(self):
        if os.path.isfile(sNoPermissionFile):
            os.remove(sNoPermissionFile)

    def test_file_not_found(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', 'no_file.vhd'])
        except subprocess.CalledProcessError as e:
            exit_status: int = e.returncode

        self.assertEqual(exit_status, 1)

    @unittest.skipIf('SUDO_UID' in os.environ.keys() or os.geteuid() == 0, "We are root. Root always has permissions so test will fail.")
    def test_file_no_permission(self):
        pathlib.Path(sNoPermissionFile).touch(mode=0o222, exist_ok=True)

        try:
            subprocess.check_output(['bin/vsg', '-f', sNoPermissionFile])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sOutputNoPermission).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)

    def test_file_empty(self):
        try:
            subprocess.check_output(['bin/vsg', '-f', 'vsg/tests/source_file/' + sEmptyFile])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sOutputEmptyFile).read_text().split('\n')

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)
