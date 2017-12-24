import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','package','package_test_input.vhd'))

class testVhdlFilePackageMethods(unittest.TestCase):


    def test_insidePackage_assignment(self):
        lExpected = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insidePackage:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPackageKeyword_assignment(self):
        lExpected = [2,18,32,47,60]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPackage_assignment(self):
        lExpected = [15,31,45,58,73]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_packageIndent_assignment(self):
#        lExpected = [2,    ,4,5,6,7,8,9,10,11,12,13,  14,15,18,  19,20,21,22,23,24,25,26,27,28,29,  30,31,32,  33,34,35,36,37,38,39,40,41,42,43,  44,45,47,48,49,50,51,52,53,54,55,56,57,58,60,  61,62,63,64,65,66,67,68,69,70,71,  72,73]
        lExpected =  [0,None,1,2,3,2,2,3, 3, 3, 2, 1,None, 0, 0,None, 1, 2, 3, 2, 2, 3, 3, 3, 2, 1,None, 0, 0,None, 1, 2, 3, 2, 2, 3, 3, 3, 2, 1,None, 0, 0, 1, 2, 3, 2, 2, 3, 3, 3, 2, 1, 0, 0,None, 1, 2, 3, 2, 2, 3, 3, 3, 2, 1,None, 0]
        # Generic actual list
        lActual = []
        for oLine in oFile.lines:
            if oLine.insidePackage:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
