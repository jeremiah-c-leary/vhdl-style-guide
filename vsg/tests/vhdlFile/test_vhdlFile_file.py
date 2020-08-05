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

    def test_file_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((4,0))
        lExpected.append((6,0))
        lExpected.append((8,0))

        utils.validate_token(self, oFile, lExpected, file_declaration.keyword)

    def test_file_identifier(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((4,2))
        lExpected.append((6,2))
        lExpected.append((8,2))
        lExpected.append((8,5))
        lExpected.append((8,8))

        utils.validate_token(self, oFile, lExpected, file_declaration.identifier)

    def test_file_comma(self):
        lExpected = []
        lExpected.append((8,3))
        lExpected.append((8,6))

        utils.validate_token(self, oFile, lExpected, file_declaration.comma)

    def test_file_colon(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((4,4))
        lExpected.append((6,4))
        lExpected.append((8,10))

        utils.validate_token(self, oFile, lExpected, file_declaration.colon)

    def test_file_subtype_indication(self):
        lExpected = []
        lExpected.append((2,6))
        lExpected.append((4,6))
        lExpected.append((6,6))
        lExpected.append((8,12))

        utils.validate_token(self, oFile, lExpected, file_declaration.subtype_indication)

    def test_file_open_keyword(self):
        lExpected = []
        lExpected.append((6,8))
        lExpected.append((8,14))

        utils.validate_token(self, oFile, lExpected, file_declaration.open_keyword)

    def test_file_open_kind_expression(self):
        lExpected = []
        lExpected.append((6,10))
        lExpected.append((8,16))

        utils.validate_token(self, oFile, lExpected, file_declaration.open_kind_expression)

    def test_file_is_keyword(self):
        lExpected = []
        lExpected.append((4,8))
        lExpected.append((6,12))
        lExpected.append((8,18))

        utils.validate_token(self, oFile, lExpected, file_declaration.is_keyword)

    def test_file_logical_name(self):
        lExpected = []
        lExpected.append((4,10))
        lExpected.append((6,14))
        lExpected.append((8,20))

        utils.validate_token(self, oFile, lExpected, file_declaration.logical_name)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((2,7))
        lExpected.append((4,11))
        lExpected.append((6,15))
        lExpected.append((8,21))

        utils.validate_token(self, oFile, lExpected, file_declaration.semicolon)

