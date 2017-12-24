import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFileCompress = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_compressed_line_test_input.vhd'))

class testVhdlFileIfAssignments(unittest.TestCase):


    def test_insideIf_assignment(self):
        lExpected = [8,13,14,19,20,21,24,30,31,32,33,41,42,43,46,52,53,54,57,66,67,68,73,80,91,98,99,100,105,107,108,109,112,114,115]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideIf:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isElseIfKeyword_assignment(self):
        lExpected = [24,73,99,100,108,114]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isElseIfKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndIfKeyword_assignment(self):
        lExpected = [11,17,27,36,39,49,50,60,62,78,89,96,103,105,110,117]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndIfKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isIfKeyword_assignment(self):
        lExpected = [8,13,19,30,33,41,46,52,57,66,80,91,98,105,107,112]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isIfKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isThenKeyword_assignment(self):
        lExpected = [8,14,21,24,32,33,43,46,54,57,68,73,80,91,98,99,100,105,107,109,112,115]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isThenKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isElseKeyword_assignment(self):
        lExpected = [85,94,102,105,109]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isElseKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ifIndent_assignment(self):
        self.maxDiff = None
#       lExpected = [   0,   1,2,   3,4,   5,6,7,8,9,10,11,  12,13,  14,15,16,17,  18,19,  20,  21,22,23,24,25,26,27,  28,  29]
        lExpected = [None,None,0,None,0,None,1,1,2,3, 3, 2,None, 2,None, 3, 3, 2,None, 2,None,None, 3, 3, 2, 3, 3, 2,None,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_compressed_line_assignment(self):
        self.assertTrue(oFileCompress.lines[10].insideIf)
        self.assertTrue(oFileCompress.lines[10].isElseKeyword)
        self.assertTrue(oFileCompress.lines[10].isElseIfKeyword)
        self.assertTrue(oFileCompress.lines[10].isEndIfKeyword)
        self.assertTrue(oFileCompress.lines[10].isIfKeyword)
        self.assertTrue(oFileCompress.lines[10].isThenKeyword)

        self.assertTrue(oFileCompress.lines[12].insideIf)
        self.assertTrue(oFileCompress.lines[12].isElseKeyword)
        self.assertTrue(oFileCompress.lines[12].isElseIfKeyword)
        self.assertTrue(oFileCompress.lines[12].isEndIfKeyword)
        self.assertTrue(oFileCompress.lines[12].isIfKeyword)
        self.assertTrue(oFileCompress.lines[12].isThenKeyword)
