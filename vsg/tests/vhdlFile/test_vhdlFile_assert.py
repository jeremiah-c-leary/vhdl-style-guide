import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','assert_statement','assert_test_input.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_isAssertKeyword_assignment(self):
        lExpected = [6,10,15,19]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isAssertKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isAssertEnd_assignment(self):
        lExpected = [8,12,17,21]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isAssertEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideAssert_assignment(self):
        lExpected = [6,7,8,10,11,12,15,16,17,19,20,21]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideAssert:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
