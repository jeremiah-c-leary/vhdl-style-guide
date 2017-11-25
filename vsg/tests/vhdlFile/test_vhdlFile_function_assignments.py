import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','function','function_test_input.vhd'))

class testVhdlFileFunctionAssignments(unittest.TestCase):


    def test_isFunctionKeyword(self):
        lExpected = [4,16,21,28,36,47]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionBegin(self):
        lExpected = [5,17,22,31,37,50]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionEnd(self):
        lExpected = [13,19,24,33,45,52]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideFunction(self):
        lExpected = [4,5,6,7,8,9,10,11,12,13,16,17,18,19,21,22,23,24,28,29,30,31,32,33,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideFunction:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionReturn(self):
        lExpected = [8,10,18,23,51]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionReturn:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_FunctionIndent(self):
        #           [   0,   1,2,   3,4,5,   6,7,8,9,10,11,  12,13,  14]
        lExpected = [None,None,0,None,1,1,None,2,3,2, 3, 2,None, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
