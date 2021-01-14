import os
import pathlib
import unittest
import sys
import subprocess
sys.path.append('vsg')

from vsg.rules import source_file
from vsg import vhdlFile
from vsg.tests import utils

sNoPermissionFile = 'no_permission.vhd'

class testOSError(unittest.TestCase):

    def tearDown(self):
        if os.path.isfile(sNoPermissionFile):
            os.remove(sNoPermissionFile)

    def test_file_not_found(self):
        sExpected = 'ERROR: encountered FileNotFoundError, No such file or directory : no_file.vhd\n'
        try:
            sActual = subprocess.check_output(['bin/vsg', '--file', 'no_file.vhd'])
        except subprocess.CalledProcessError as e:
            sActual = str(e.output.decode('utf-8'))
            iExitStatus = e.returncode

        self.assertEqual(sActual, sExpected)
        self.assertEqual(iExitStatus, 1)

    def test_file_no_permission(self):
        pathlib.Path(sNoPermissionFile).touch(mode=0o222, exist_ok=True)

        sExpected = 'ERROR: encountered PermissionError, Permission denied : no_permission.vhd\n'
        try:
            sActual = subprocess.check_output(['bin/vsg', '--file', sNoPermissionFile])
        except subprocess.CalledProcessError as e:
            sActual = str(e.output.decode('utf-8'))
            iExitStatus = e.returncode

        self.assertEqual(sActual, sExpected)
        self.assertEqual(iExitStatus, 1)

