import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','file_statement','file_test_input.vhd'))

class testVhdlFileFileMethods(unittest.TestCase):

    def test_isFileKeyword_assignment(self):
        lExpected = [4,6,9,11]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFileKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFileEnd_assignment(self):
        lExpected = [4,7,9,12]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFileEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideFile_assignment(self):
        lExpected = [4,6,7,9,11,12]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideFile:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
