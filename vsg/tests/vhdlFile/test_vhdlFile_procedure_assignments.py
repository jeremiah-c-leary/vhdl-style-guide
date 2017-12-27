import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','procedure','procedure_test_input.vhd'))

class testVhdlFileProcedureAssignments(unittest.TestCase):


    def test_isProcedureKeyword(self):
        lExpected = [4,6,14,16,26,30,40,44]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureBegin(self):
        lExpected = [27,35,41,49]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcedureEnd(self):
        lExpected = [4,10,14,20,28,36,42,50]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcedure(self):
        lExpected = [4,6,7,8,9,10,14,16,17,18,19,20,26,27,28,30,31,32,33,34,35,36,40,41,42,44,45,46,47,48,49,50]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideProcedure:
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
        lExpected = [7,8,9,10,17,18,19,20,31,32,33,34,44,45,46,47,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcedureParameter:
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
