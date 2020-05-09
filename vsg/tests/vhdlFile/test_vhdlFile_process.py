import os
from pprint import pprint

import unittest
from vsg import vhdlFile
from vsg.tests import utils

sFileLibraryName = os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd')
lFileLibrary = utils.read_vhdlfile(sFileLibraryName)
oFileLibrary = vhdlFile.vhdlFile(lFileLibrary)

lFileProcessIs = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_is_test_input.vhd'))
oFileProcessIs = vhdlFile.vhdlFile(lFileProcessIs)

lFileProcess = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(lFileProcess)


class testVhdlFileMethods(unittest.TestCase):

    def test_comment_assignment(self):
        lExpected = [8,21,50,76,83,90,114,134,135,136,137,138]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isComment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcess_assignment(self):
        lExpected = [6,7,8,9,11,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42,46,47,48,51,52,53,55,56,57,58,59,60,63,64,65,68,69,70,71,72,75,76,77,78,79,81,82,83,84,85,86,88,89,90,91,92,93,94,97,98,99,100,101,102,103,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132]
        # Generic actual list
        lExpected.extend(range(140, 151))
        lExpected.extend(range(152,156))
        lExpected.extend(range(157,168))
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.insideProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessBegin_assignment(self):
        lExpected = [6,13,20,28,34,40,47,52,59,64,70,77,84,92,101,121,130,148,153,165]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessKeyword_assignment(self):
        lExpected = [6,11,17,24,32,38,46,51,55,63,68,75,81,88,97,116,125,140,152,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessLabel_assignment(self):
        lExpected = [46,63,68,75,81,88,97,116,140,152,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessEndLabel_assignment(self):
        lExpected = [48,65,72,79,86,94,103,123,150,155,167]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessEndLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndProcess_assignment(self):
        lExpected = [9,15,22,30,36,42,48,53,60,65,72,79,86,94,103,123,132,150,155,167]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isEndProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideSensitivityList_assignment(self):
        lExpected = [6,11,12,17,18,19,24,25,26,27,32,33,38,39,46,51,55,56,57,63,68,75,81,88,97,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.insideSensitivityList:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSensitivityListBegin_assignment(self):
        lExpected = [6,11,17,24,32,38,46,51,55,63,68,75,81,88,97,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isSensitivityListBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSensitivityListEnd_assignment(self):
        lExpected = [6,12,19,27,33,39,46,51,57,63,68,75,81,88,97,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isSensitivityListEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_end_architecture_assignment(self):
        lExpected = [169]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_indent_level_attribute(self):
        self.assertEqual(1, oFileProcess.lines[97].indentLevel)
        self.assertEqual(None, oFileProcess.lines[98].indentLevel)
        self.assertEqual(2, oFileProcess.lines[99].indentLevel)
        self.assertEqual(None, oFileProcess.lines[100].indentLevel)
        self.assertEqual(1, oFileProcess.lines[101].indentLevel)
        self.assertEqual(None, oFileProcess.lines[102].indentLevel)
        self.assertEqual(1, oFileProcess.lines[103].indentLevel)

        self.assertEqual(1, oFileProcess.lines[116].indentLevel)
        self.assertEqual(None, oFileProcess.lines[117].indentLevel)
        self.assertEqual(2, oFileProcess.lines[118].indentLevel)
        self.assertEqual(2, oFileProcess.lines[119].indentLevel)
        self.assertEqual(None, oFileProcess.lines[120].indentLevel)
        self.assertEqual(1, oFileProcess.lines[121].indentLevel)
        self.assertEqual(None, oFileProcess.lines[122].indentLevel)
        self.assertEqual(1, oFileProcess.lines[121].indentLevel)

        self.assertEqual(1, oFileProcess.lines[125].indentLevel)
        self.assertEqual(None, oFileProcess.lines[126].indentLevel)
        self.assertEqual(2, oFileProcess.lines[127].indentLevel)
        self.assertEqual(2, oFileProcess.lines[128].indentLevel)
        self.assertEqual(None, oFileProcess.lines[129].indentLevel)
        self.assertEqual(1, oFileProcess.lines[130].indentLevel)

        self.assertEqual(1, oFileProcess.lines[140].indentLevel)
        self.assertEqual(None, oFileProcess.lines[141].indentLevel)
        self.assertEqual(2, oFileProcess.lines[142].indentLevel)
        self.assertEqual(3, oFileProcess.lines[143].indentLevel)
        self.assertEqual(2, oFileProcess.lines[144].indentLevel)
        self.assertEqual(2, oFileProcess.lines[145].indentLevel)
        self.assertEqual(2, oFileProcess.lines[146].indentLevel)
        self.assertEqual(None, oFileProcess.lines[147].indentLevel)
        self.assertEqual(1, oFileProcess.lines[148].indentLevel)
        self.assertEqual(None, oFileProcess.lines[149].indentLevel)
        self.assertEqual(1, oFileProcess.lines[150].indentLevel)

        self.assertEqual(None, oFileProcess.lines[151].indentLevel)

        self.assertEqual(1, oFileProcess.lines[152].indentLevel)
        self.assertEqual(1, oFileProcess.lines[153].indentLevel)
        self.assertEqual(None, oFileProcess.lines[154].indentLevel)
        self.assertEqual(1, oFileProcess.lines[155].indentLevel)

        self.assertEqual(None, oFileProcess.lines[156].indentLevel)

#        print(pprint(oFileProcess.lines[155].__dict__, indent=2))
#        print(pprint(oFileProcess.lines[156].__dict__, indent=2))
#        print(pprint(oFileProcess.lines[157].__dict__, indent=2))

        self.assertEqual(1, oFileProcess.lines[157].indentLevel)
        self.assertEqual(None, oFileProcess.lines[158].indentLevel)
        self.assertEqual(2, oFileProcess.lines[159].indentLevel)
        self.assertEqual(3, oFileProcess.lines[160].indentLevel)
        self.assertEqual(2, oFileProcess.lines[161].indentLevel)
        self.assertEqual(2, oFileProcess.lines[162].indentLevel)
        self.assertEqual(2, oFileProcess.lines[163].indentLevel)
        self.assertEqual(None, oFileProcess.lines[164].indentLevel)
        self.assertEqual(1, oFileProcess.lines[165].indentLevel)
        self.assertEqual(None, oFileProcess.lines[166].indentLevel)
        self.assertEqual(1, oFileProcess.lines[167].indentLevel)
        self.assertEqual(None, oFileProcess.lines[168].indentLevel)


    def test_isProcessIs_assignment(self):
        lExpected = [6,11,16,19,22,26,30]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcessIs.lines):
            if oLine.isProcessIs:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

