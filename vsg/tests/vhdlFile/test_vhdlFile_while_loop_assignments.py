import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','while_loop','while_loop_test_input.vhd'))

class testVhdlFileWhileLoopAssignments(unittest.TestCase):

    def test_insideWhileLoop(self):
        lExpected = [9,10,11,13,14,15,17,18,19]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideWhileLoop:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isWhileLoopKeyword(self):
        lExpected = [9,13,17]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWhileLoopKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isWhileLoopEnd(self):
        lExpected = [11,15,19]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWhileLoopEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_WhileLoopIndent(self):
        #           [   0,   1,2,   3,4,5,6,7,   8,9,10,11,  12]
        lExpected = [None,None,0,None,1,2,1,2,None,2, 3, 2,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
