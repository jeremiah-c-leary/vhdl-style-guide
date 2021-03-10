import pathlib
import subprocess
import shutil
import os

import unittest

from vsg import __main__
from vsg import severity

sFileName = 'context_classification_test_input.vhd'
sFixedFileName = 'context_classification_test_input.fixed.vhd'

sFile = os.path.join(os.path.dirname(__file__), sFileName)
sFixedFile = os.path.join(os.path.dirname(__file__), sFixedFileName)

oSeverityList = severity.create_list({})


class test_context_using_main(unittest.TestCase):

    def setUp(self):
        if os.path.isfile(sFileName):
            os.remove(sFileName)
        shutil.copyfile(sFile, sFileName)

    def tearDown(self):
        os.remove(sFileName)

    def test_classification_file(self):
        self.maxDiff = None
        subprocess.check_output(['bin/vsg', '-f', sFileName, '--fix']).decode('utf-8').split('\n')

        lActual = pathlib.Path(sFileName).read_text().split('\n')
        lExpected = pathlib.Path(sFixedFile).read_text().split('\n')

        self.assertEqual(lExpected, lActual)
