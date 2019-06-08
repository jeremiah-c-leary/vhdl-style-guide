import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFileConstant = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))
oFileConstant = vhdlFile.vhdlFile(lFileConstant)

class testVhdlFileConstantMethods(unittest.TestCase):

    def test_isConstant_assignment(self):
        lExpected = [5,6,7,8,9,10,17,18,28,30,38,40,43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstantEnd_assignment(self):
        lExpected = [5,6,7,8,9,11,17,18,28,36,38,41,44]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstantEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideConstant_assignment(self):
        lExpected = [5,6,7,8,9,10,11,17,18,28,30,31,32,33,34,35,36,38]
        lExpected.extend(range(40, 42))
        lExpected.extend(range(43, 45))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.insideConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstantArray_assignment(self):
        lExpected = []
        lExpected.extend(range(30,37))
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstantArray:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
