# -*- coding: utf-8 -*-
import os
import pathlib
import stat
import subprocess
import sys
import unittest
from tempfile import TemporaryDirectory
from unittest import mock

sys.path.append("vsg")

from tests import utils
from vsg import __main__, vhdlFile
from vsg.rules import source_file

sNoPermissionFile = "no_permission.vhd"
sEmptyFile = "empty_file.vhd"

sOutputNoFile = os.path.join(os.path.dirname(__file__), "output_no_file.txt")
sOutputNoPermission = os.path.join(os.path.dirname(__file__), "output_no_permission.txt")
sOutputEmptyFile = os.path.join(os.path.dirname(__file__), "output_empty_file.txt")


class testOSError(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_file_not_found(self):
        try:
            subprocess.check_output([*utils.vsg_exec(), "-f", "no_file.vhd"], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            exit_status: int = e.returncode

        self.assertEqual(exit_status, 1)

    @unittest.skipIf(utils.is_user_admin(), "We are root. Root always has permissions so test will fail.")
    @unittest.skipIf(utils.is_windows(), "Permissions can not be tested on windows.")
    def test_file_no_permission(self):
        sNoPermissionTempFile = os.path.join(self._tmpdir.name, sNoPermissionFile)

        pathlib.Path(sNoPermissionTempFile).touch(mode=0o222, exist_ok=True)

        try:
            subprocess.check_output([*utils.vsg_exec(), "-f", sNoPermissionTempFile])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sOutputNoPermission).read_text().splitlines()

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_token(utils.replace_total_count(lActual), sNoPermissionTempFile, sNoPermissionFile), lExpected)

    def test_file_empty(self):
        try:
            subprocess.check_output([*utils.vsg_exec(), "-f", "tests/source_file/" + sEmptyFile])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        lExpected = pathlib.Path(sOutputEmptyFile).read_text().splitlines()

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(utils.replace_total_count(lActual), lExpected)
