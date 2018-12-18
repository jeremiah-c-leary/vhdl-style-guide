import os

import unittest
from vsg import vhdlFile

oFileConstant = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))

class testVhdlFileConstantMethods(unittest.TestCase):

    def test_isConstant_assignment(self):
        lExpected = [5,6,7,8,9,10,17,18,28,30]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstantEnd_assignment(self):
        lExpected = [5,6,7,8,9,11,17,18,28,36]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstantEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideConstant_assignment(self):
        lExpected = [5,6,7,8,9,10,11,17,18,28,30,31,32,33,34,35,36]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.insideConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
