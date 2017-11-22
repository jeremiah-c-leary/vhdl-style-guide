import os

import unittest
from vsg import vhdlFile

oFileVariable = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_isVariable_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileVariable.lines):
            if oLine.isVariable:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
