import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','function','function_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileMultiple = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','function','function_multiple_parameters_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(lFileMultiple)

class testVhdlFileFunctionAssignments(unittest.TestCase):

    def test_isFunctionKeyword(self):
        lExpected = [4,16,21,28,36,47,54,63,70,78,87,97,110,126,128,136,141,146]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionBegin(self):
        lExpected = [5,17,22,31,37,50,57,66,74,83,93,104,115,137,142,147]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionEnd(self):
        lExpected = [13,19,24,33,45,52,59,68,76,85,95,106,117,126,130,139,144,149]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideFunction(self):
        lExpected = [4,5,6,7,8,9,10,11,12,13,16,17,18,19,21,22,23,24,28,29,30,31,32,33,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,54,55,56,57,58,59,63,64,65,66,67,68,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106,110,111,112,113,114,115,116,117,126,128,129,130]
        lExpected.extend(range(136, 140))
        lExpected.extend(range(141,145))
        lExpected.extend(range(146,150))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideFunction:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionReturn(self):
        lExpected = [8,10,18,23,51,58,67,75,84,94,105,116,126,130,138,143,148]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionReturn:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_hasFunctionReturnType(self):
        lExpected = [4,16,21,30,36,47,54,65,73,82,91,101,112,126,130,136,141,146]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasFunctionReturnType:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_FunctionIndent(self):
        #           [   0,   1,2,   3,4,5,   6,7,8,9,10,11,  12,13,  14]
        lExpected = [None,None,0,None,1,1,None,2,3,2, 3, 2,None, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_FunctionParameterEndIndent(self):
        #           [  17,18,19,20,21,22,23,24,  25,26,27,28,29,30,  31,32,33,34,35,  36,37]
        lExpected = [None, 1, 2, 2, 2, 2, 2, 1,None, 1, 1, 2, 2, 1,None, 1, 2, 2, 1,None, 0]
        # Generic actual list
        lActual = []
        iMinCheck = 17
        iMaxCheck = iMinCheck + len(lExpected)
        for iIndex, oLine in enumerate(oFileMultiple.lines):
            if iIndex == iMaxCheck:
                break
            if iIndex >= iMinCheck:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionParameter(self):
        lExpected = [4,16,21,28,29,36,47,54,63,64,65,70,71,72,78,79,80,87,88,89,97,98,99,110,111,112,126,128,129,130]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isFunctionParameter:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFunctionParameterMultiple(self):
        lExpected = [4,5,6,7,19,20,21,22,23,28,29,33,34]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiple.lines):
            if oLine.isFunctionParameter:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_is_not_constant(self):
        lExpected = []
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiple.lines):
            if oLine.isConstant:
                lActual.append(iIndex)  # pragma: no cover
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_is_not_signal(self):
        lExpected = []
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiple.lines):
            if oLine.isSignal:
                lActual.append(iIndex)  # pragma: no cover
        # Compare
        self.assertEqual(lActual, lExpected)
