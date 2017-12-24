import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','variable_assignment','variable_assignment_test_input.vhd'))

class testVhdlFileVariableAssignmentAssignments(unittest.TestCase):


    def test_isVariableAssignment_assignment(self):
        lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90,92,99]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideVariableAssignment_assignment(self):
        lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,53,54,55,56,57,58,63,65,66,71,73,74,75,80,81,83,88,89,90,92,93,94,95,99,100]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideVariableAssignment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isVariableAssignmentEnd_assignment(self):
        lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,55,56,58,63,65,66,71,74,75,80,81,83,88,89,90,95,100]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignmentEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_variableAssignmentAlignmentColumn_assignment(self):
        #lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
        lExpected =  [18, 4, 6,11,10,10,12,10, 8,10,10, 9,10, 9, 8, 7, 8,10,12,13,10,15,14,10, 8,12,10, 8,11,10, 6]
        # Generic actual list
        lActual = []
        for oLine in oFile.lines:
            if oLine.isVariableAssignment:
                lActual.append(oLine.variableAssignmentAlignmentColumn)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_variableAssignmentIndentLevel_assignment(self):
        #lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
        lExpected =  [ 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 4, 5, 5, 4, 5, 5, 4, 4, 5, 4, 4, 4, 4, 2]
        # Generic actual list
        lActual = []
        for oLine in oFile.lines:
            if oLine.isVariableAssignment:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
