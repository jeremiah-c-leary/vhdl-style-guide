import os

import unittest
from vsg import vhdlFile

oFileBlock = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','block','block_test_input.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_insideBlock_assignment(self):
        lExpected = [7,8,9,10]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileBlock.lines):
            if oLine.insideBlock:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isBlockBegin_assignment(self):
        lExpected = [9]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileBlock.lines):
            if oLine.isBlockBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isBlockKeyword_assignment(self):
        lExpected = [7]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileBlock.lines):
            if oLine.isBlockKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndBlock_assignment(self):
        lExpected = [10]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileBlock.lines):
            if oLine.isEndBlock:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_block_indent_assignment(self):
        self.maxDiff = None
#       lExpected = [   0,   1,2,   3,4,   5,6,7,8,9,10,  11,12,  13]
        lExpected = [None,None,0,None,0,None,1,1,2,1, 1,None, 0,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFileBlock.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
