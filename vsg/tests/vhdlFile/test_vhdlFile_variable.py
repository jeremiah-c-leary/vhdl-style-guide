import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFileVariable = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))
oFileVariable = vhdlFile.vhdlFile(lFileVariable)

class testVhdlFileMethods(unittest.TestCase):

    def test_isVariable_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,27,28,29,37,38,39,47,48,49]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileVariable.lines):
            if oLine.isVariable:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
