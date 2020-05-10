import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generate','generate_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generate','generate_2008_test_input.vhd'))
o2008File = vhdlFile.vhdlFile(lFile)

class testVhdlFileGenerateAssignments(unittest.TestCase):


    def test_isGenerateKeyword(self):
        lExpected = [6,11,16,21,26,31,36,41,46,51,56,60,65,68,71,77,83,88,90,94,105]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateBegin(self):
        lExpected = [7,12,17,22,27,32,37,42,47,52,84]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateEnd(self):
        lExpected = [9,14,19,24,29,34,39,44,49,54,58,62,73,75,79,81,86,96,98,100,106]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture(self):
        lExpected = [108]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_GenerateIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,  10,11,12,13,14,  15]
        lExpected = [None,None,0,None,0,None,1,1,2,1,None, 1, 1, 2, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideGenerate(self):
        lExpected = [6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,56,57,58,60,61,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,85,86]
        lExpected.extend(range(88, 101))
        lExpected.extend(range(104, 107))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideGenerate:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateLabel(self):
        lExpected = [6,11,16,21,26,31,36,41,46,51,56,60,65,68,71,77,83,88,90,94,104]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateEndLabel(self):
        lExpected = [9,14,19,29,34,39,44,49,54,58,62,73,75,79,81,86,96,98,100,106]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEndLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideGenerateCase(self):
        lExpected = []
        lExpected.extend(range(7, 29))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(o2008File.lines):
            if oLine.insideGenerateCase:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_2008_insideGenerate(self):
        lExpected = range(7, 29)
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(o2008File.lines):
            if oLine.insideGenerate:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateCaseWhen(self):
        lExpected = [9,11,19]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(o2008File.lines):
            if oLine.isGenerateCaseWhen:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_2008_insideGenerate(self):
        self.assertTrue(o2008File.lines[7].insideGenerate)
        self.assertTrue(o2008File.lines[7].insideGenerateCase)
        self.assertTrue(o2008File.lines[7].isGenerateKeyword)
        self.assertTrue(o2008File.lines[7].isGenerateLabel)
        self.assertFalse(o2008File.lines[7].insideInstantiation)
        self.assertFalse(o2008File.lines[7].insideCase)

        self.assertFalse(o2008File.lines[9].insideCase)
        self.assertFalse(o2008File.lines[9].isCaseWhenKeyword)

    def test_2008_case_generate_indent(self):
        self.assertEqual(o2008File.lines[5].indentLevel, 0)
        self.assertEqual(o2008File.lines[6].indentLevel, None)
        self.assertEqual(o2008File.lines[7].indentLevel, 1)
        self.assertEqual(o2008File.lines[8].indentLevel, 2)
        self.assertEqual(o2008File.lines[9].indentLevel, 2)
        self.assertEqual(o2008File.lines[10].indentLevel, 3)
        self.assertEqual(o2008File.lines[11].indentLevel, 2)
        self.assertEqual(o2008File.lines[12].indentLevel, 3)
        self.assertEqual(o2008File.lines[13].indentLevel, 3)
        self.assertEqual(o2008File.lines[14].indentLevel, 3)
        self.assertEqual(o2008File.lines[15].indentLevel, 4)
        self.assertEqual(o2008File.lines[16].indentLevel, 5)
        self.assertEqual(o2008File.lines[17].indentLevel, 4)
        self.assertEqual(o2008File.lines[18].indentLevel, 3)
        self.assertEqual(o2008File.lines[19].indentLevel, 2)
        self.assertEqual(o2008File.lines[20].indentLevel, 3)
        self.assertEqual(o2008File.lines[21].indentLevel, 3)
        self.assertEqual(o2008File.lines[22].indentLevel, 3)
        self.assertEqual(o2008File.lines[23].indentLevel, 4)
        self.assertEqual(o2008File.lines[24].indentLevel, 5)
        self.assertEqual(o2008File.lines[25].indentLevel, 5)
        self.assertEqual(o2008File.lines[26].indentLevel, 4)
        self.assertEqual(o2008File.lines[27].indentLevel, 3)
        self.assertEqual(o2008File.lines[28].indentLevel, 1)
        self.assertEqual(o2008File.lines[29].indentLevel, None)
        self.assertEqual(o2008File.lines[30].indentLevel, 0)
