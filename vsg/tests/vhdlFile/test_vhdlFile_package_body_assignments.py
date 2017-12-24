import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','package_body','package_body_test_input.vhd'))

class testVhdlFilePackageBodyMethods(unittest.TestCase):


    def test_insidePackageBody_assignment(self):
        lExpected = [7,8,9]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insidePackageBody:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPackageBodyKeyword_assignment(self):
        lExpected = [7]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPackageBodyKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPackageBodyEnd_assignment(self):
        lExpected = [9]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPackageBodyEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_package_bodyIndent_assignment(self):
#        lExpected = [7,   8,9]
        lExpected =  [0,None,0]
        # Generic actual list
        lActual = []
        for oLine in oFile.lines:
            if oLine.insidePackageBody:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
