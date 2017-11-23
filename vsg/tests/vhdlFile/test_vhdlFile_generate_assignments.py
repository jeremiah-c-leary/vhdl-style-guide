import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','generate','generate_test_input.vhd'))

class testVhdlFileGenerateAssignments(unittest.TestCase):


    def test_isGenerateKeyword(self):
        lExpected = [6,11,16,21,26,31,36,41,46,51,56,60]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateBegin(self):
        lExpected = [7,12,17,22,27,32,37,42,47,52]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateEnd(self):
        lExpected = [9,14,19,24,29,34,39,44,49,54,58,62]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_GenerateIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,  10,11,12,13,14,  15]
        lExpected = [None,None,0,None,0,None,1,1,2,1,None, 1, 1, 2, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
