# -*- coding: utf-8 -*-
import os
import pathlib
import shutil
import subprocess
import unittest
from tempfile import TemporaryDirectory

from tests import utils
from vsg import __main__, severity

sFileName = "context_classification_test_input.vhd"
sFixedFileName = "context_classification_test_input.fixed.vhd"

sFile = os.path.join(os.path.dirname(__file__), sFileName)
sFixedFile = os.path.join(os.path.dirname(__file__), sFixedFileName)

oSeverityList = severity.create_list({})


class test_context_using_main(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

        self._sFileName = os.path.join(self._tmpdir.name, sFileName)
        shutil.copyfile(sFile, self._sFileName)

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_classification_file(self):
        self.maxDiff = None
        subprocess.check_output([*utils.vsg_exec(), "-f", self._sFileName, "--fix"]).decode("utf-8").splitlines()

        lActual = pathlib.Path(self._sFileName).read_text().splitlines()
        lExpected = pathlib.Path(sFixedFile).read_text().splitlines()

        self.assertEqual(lExpected, lActual)
