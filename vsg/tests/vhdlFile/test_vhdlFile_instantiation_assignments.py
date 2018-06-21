import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_generic_test_input.vhd'))
oFileGenerate = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_generate_test_input.vhd'))
oFileDirect = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_direct_test_input.vhd'))

class testVhdlFileInstantiationAssignments(unittest.TestCase):


    def test_isInstantiation_assignment(self):
        lExpected = [6,17,23,29,36,44,52,57,63,69,75,82,91]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideInstantiation_assignment(self):
        lExpected = [6,7,8,9,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,52,53,54,55,57,58,59,60,61,63,64,65,66,69,70,71,72,73,75,76,77,78,79,80,82,83,84,85,86,87,88,89,91,92,93,94,95,96]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideInstantiation:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationPortKeyword_assignment(self):
        lExpected = [7,18,24,31,37,45,52,58,64,70,76,83,92]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationPortEnd_assignment(self):
        lExpected = [11,22,28,35,42,50,55,61,66,73,80,89,96]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationPortAssignment_assignment(self):
        lExpected = [8,9,10,19,20,21,25,26,27,32,33,34,39,41,46,47,48,53,54,55,58,59,60,65,71,72,77,78,79,85,86,87,88,94,95]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationGenericKeyword_assignment(self):
        lExpected = [7,22,33,44,54,63,73,81]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isInstantiationGenericKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationGenericEnd_assignment(self):
        lExpected = [10,25,36,46,56,65,73,85]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isInstantiationGenericEnd:
                lActual.append(iIndex)
        # Compare
#        utils.print_attributes(oFileGeneric.lines[81])
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationGenericAssignment_assignment(self):
        lExpected = [8,9,23,24,34,35,45,46,54,55,64,65,83,84]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isInstantiationGenericAssignment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationIdention_assignment(self):
        self.maxDiff = None
        #lExpected = [ 6, 7, 8, 9,10,11,12,13,14,15,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,80,81,  82,83,84,85,86,  87,88,89,90,91]
        lExpected =  [ 1, 2, 3, 3, 2, 2, 3, 3, 3, 2, 1, 2, 3, 3, 2, 2, 3, 3, 3, 2, 1, 2, 3, 3, 2, 2, 3, 3, 3, 2, 1, 2, 3, 3, 2, 3, 3, 3, 2, 1, 2, 3, 2, 2, 3, 3, 3, 2, 1, 3, 3, 2, 3, 3, 3, 2, 1, 2, 2, 3, 3, 3, 2, 1, 2,None, 3, 3, 2, 2,None, 3, 3, 3, 2]
        # Generic actual list
        lActual = []
        for oLine in oFileGeneric.lines:
            if oLine.insideInstantiation:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiation_assignment_inside_generate(self):
        lExpected = [8]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGenerate.lines):
            if oLine.isInstantiationDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isDirectInstantiation_assignment_inside_generate(self):
        lExpected = [6,13,20]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileDirect.lines):
            if oLine.isDirectInstantiationDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

        lExpected = [27]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileDirect.lines):
            if oLine.isInstantiationDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
