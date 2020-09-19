
import shutil
import sys
import os


import unittest
from unittest import mock

from vsg import __main__
from vsg.tests import utils

sFileName = 'context_reference_classification_test_input.vhd'
sFixedFileName = 'context_reference_classification_test_input.fixed.vhd'

sFile = os.path.join(os.path.dirname(__file__), sFileName)
sFixedFile = os.path.join(os.path.dirname(__file__), sFixedFileName)


class test_context_reference_using_main(unittest.TestCase):

    def setUp(self):
        if os.path.isfile(sFileName):
            os.remove(sFileName)
        shutil.copyfile(sFile, sFileName)

    def tearDown(self):
        os.remove(sFileName)

    @mock.patch('sys.stdout')
    def test_classification_file(self, mock_stdout):
        self.maxDiff = None
        try:
            sys.argv =  ['vsg', '-f', sFileName, '--fix']
            __main__.main()
        except SystemExit as e:
            pass
#            self.assertEqual(e.code, 0)

        lActual = []
        utils.read_file(sFileName, lActual)

        lExpected = []
        utils.read_file(sFixedFile, lExpected)

        self.assertEqual(lExpected, lActual)
