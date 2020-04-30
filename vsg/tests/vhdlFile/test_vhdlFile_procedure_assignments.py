import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','procedure','procedure_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileProcedureAssignments(unittest.TestCase):


    def test_isProcedureKeyword(self):
        lExpected = [4,6,14,16,26,30,40,44,54,63,72,84,96,110]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureBegin(self):
        lExpected = [27,35,41,49,60,69,79,91,99,117]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureEnd(self):
        lExpected = [4,10,14,20,28,36,42,50,61,70,80,92,100,123]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcedure(self):
        lExpected = [4,6,7,8,9,10,14,16,17,18,19,20,26,27,28,30,31,32,33,34,35,36,40,41,42,44,45,46,47,48,49,50,54,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,79,80,84,85,86,87,88,89,90,91,92]
        lExpected.extend(range(96, 101))
        lExpected.extend(range(110, 124))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideProcedure:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcedureDeclarative(self):
        lExpected = [89,90,115,116]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideProcedureDeclarative:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ProcedureIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,10,  11]
        lExpected = [None,None,0,None,1,None,1,2,2,2, 2,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureParameter(self):
        lExpected = [7,8,9,10,17,18,19,20,31,32,33,34,44,45,46,47,48,55,56,57,58,64,65,66,67,73,74,75,76,85,86,87,88,97,111,112,113,114]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureParameter:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureParameterEnd(self):
        lExpected = [10,20,34,48,58,67,77,88,97,114]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureParameterEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureIs(self):
        lExpected = [26,34,40,48,59,68,78,88,98,114]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureIs:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_is_not_constant(self):
        lExpected = []
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                lActual.append(iIndex)  # pragma: no cover
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_is_not_signal(self):
        lExpected = []
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                lActual.append(iIndex)  # pragma: no cover
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ProcedureInsideProcessIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,10,  11]
        lIndex = []
        lIndex.extend(range(94, 103))
        lExpected = [1, None, 2, 3, 2, 2, 2, None, 1]
        # Generic actual list
        lActual = []
        for iIndex in range(94, 103):
            lActual.append(oFile.lines[iIndex].indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureBegin(self):
        lExpected = [125]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureEnd(self):
        lExpected = [127]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

