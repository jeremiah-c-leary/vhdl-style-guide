import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','with_statement','with_test_input.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_isWithKeyword_assignment(self):
        lExpected = [6]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWithKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
