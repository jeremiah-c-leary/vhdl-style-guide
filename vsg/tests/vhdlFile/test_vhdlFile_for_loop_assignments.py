import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','for_loop','for_loop_test_input.vhd'))

class testVhdlFileForLoopAssignments(unittest.TestCase):


    def test_isForLoopKeyword(self):
        lExpected = [9,19,21,26]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isForLoopEnd(self):
        lExpected = [11,23,24,28]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ForLoopIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,   8,9,10,11,  12,13,   14]
        lExpected = [None,None,0,None,0,None,1,1,None,2, 3, 2,None, 1, None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
