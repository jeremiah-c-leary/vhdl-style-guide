import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','attribute','attribute_test_input.vhd'))

class testVhdlFileAttributeMethods(unittest.TestCase):

    def test_isAttributeKeyword_assignment(self):
        lExpected = [4,5,9,11]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isAttributeKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isAttributeEnd_assignment(self):
        lExpected = [4,6,9,12]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isAttributeEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideAttribute_assignment(self):
        lExpected = [4,5,6,9,11,12]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideAttribute:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
