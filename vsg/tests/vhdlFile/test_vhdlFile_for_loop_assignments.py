import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','for_loop','for_loop_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileForLoopAssignments(unittest.TestCase):


    def test_isForLoopKeyword(self):
        lExpected = [9,19,21,26]
        lExpected.extend([36,40,44,48,52,56])
        lExpected.extend([66,67,68,69,72,73,79,80,83,84,98,99])
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isForLoopEnd(self):
        lExpected = [11,23,24,28]
        lExpected.extend([38,42,46,50,54,58])
        lExpected.extend([71,75,76,77,78,82,86,87,88,89])
        lExpected.extend([101,102])
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

    def test_isForLoopLabel(self):
        lExpected = [36,40,44,48,52,56]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ForLoopIndent_w_nested_loops(self):
        #           [65  ,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,   90]
        lExpected = [None, 2, 3, 4, 5, 6, 5, 5, 6, 7, 6, 5, 4, 3, 3, 4, 5, 4, 4, 5, 6, 5, 4, 3, 2, None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex > 64 and iIndex < 91:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ForLoopIndent_w_nested_loops_in_procedure_in_process_declarative(self):
        #           [95  ,96,97,98,99,100,101,102,103, 104]
        lExpected = [None, 2, 2, 3, 4,  5,  4,  3,  2,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex > 94 and iIndex < 105:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndProcedure(self):
        lExpected = [103]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideForLoop(self):
        lExpected = [98,99,100,101,102]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex > 93 and iIndex < 105:
                if oLine.insideForLoop:
                    lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

