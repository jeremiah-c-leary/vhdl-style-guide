import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import file_declaration

lFileFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','file_statement','file_test_input.vhd'))
oFileFile = vhdlFile.vhdlFile(lFileFile)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','file_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileFileFileMethods(unittest.TestCase):

    def test_isFileKeyword_assignment(self):
        lExpected = [4,6,9,11,26]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileFile.lines):
            if oLine.isFileKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isFileEnd_assignment(self):
        lExpected = [4,7,9,12,26]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileFile.lines):
            if oLine.isFileEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideFile_assignment(self):
        lExpected = [4,6,7,9,11,12,26]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileFile.lines):
            if oLine.insideFile:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_indent(self):
        lExpected = [1,None,2,None,1]
        # Generic actual list
        lActual = []
        for iIndex in range(24, 29):
            lActual.append(oFileFile.lines[iIndex].indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)
