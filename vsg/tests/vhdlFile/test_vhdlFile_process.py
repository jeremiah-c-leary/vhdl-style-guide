import os

import unittest
from vsg import vhdlFile

sFileLibraryName = os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd')
oFileLibrary = vhdlFile.vhdlFile(sFileLibraryName)

oFileProcess = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_comment_assignment(self):
        lExpected = [8,21,50,76,83,90]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isComment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcess_assignment(self):
        lExpected = [6,7,8,9,11,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42,46,47,48,51,52,53,55,56,57,58,59,60,63,64,65,68,69,70,71,72,75,76,77,78,79,81,82,83,84,85,86,88,89,90,91,92,93,94,97,98,99,100,101,102,103]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.insideProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessBegin_assignment(self):
        lExpected = [6,13,20,28,34,40,47,52,59,64,70,77,84,92,101]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessKeyword_assignment(self):
        lExpected = [6,11,17,24,32,38,46,51,55,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessLabel_assignment(self):
        lExpected = [46,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndProcess_assignment(self):
        lExpected = [9,15,22,30,36,42,48,53,60,65,72,79,86,94,103]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isEndProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideSensitivityList_assignment(self):
        lExpected = [6,11,12,17,18,19,24,25,26,27,32,33,38,39,46,51,55,56,57,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.insideSensitivityList:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSensitivityListBegin_assignment(self):
        lExpected = [6,11,17,24,32,38,46,51,55,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isSensitivityListBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSensitivityListEnd_assignment(self):
        lExpected = [6,12,19,27,33,39,46,51,57,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isSensitivityListEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
