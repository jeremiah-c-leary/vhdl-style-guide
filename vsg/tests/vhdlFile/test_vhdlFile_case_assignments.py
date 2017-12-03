import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','case','case_test_input.vhd'))


class testVhdlFileIfAssignments(unittest.TestCase):

    def test_isCaseKeyword_assignment(self):
        lExpected = [9,41,77]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseIsKeyword_assignment(self):
        lExpected = [9,43,77]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseIsKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseWhenKeyword_assignment(self):
        lExpected = [11,17,23,29,45,52,58,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndCaseKeyword_assignment(self):
        lExpected = [33,70,79]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndCaseKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideCaseWhen_assignment(self):
        lExpected = [11,17,23,29,45,46,52,58,59,60,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideCaseWhen:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseWhenEnd_assignment(self):
        lExpected = [11,17,23,29,46,52,60,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_caseIndent_assignment(self):
        self.maxDiff = None
#       lExpected = [   0,   1,2,   3,4,   5,6,7,8,9,  10,11,  12,13,14,15,  16,17,  18,19,20,21,  22,23,  24,25,26,27,  28,29, 30,31,  32,33,34,35,  36]
        lExpected = [None,None,0,None,0,None,1,1,2,2,None, 3,None, 4, 4, 4,None, 3,None, 4, 4, 4,None, 3,None, 4, 4, 4,None,3,None, 4,None, 2, 2, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseNull_assignment(self):
        lExpected = [31,68]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseNull:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
