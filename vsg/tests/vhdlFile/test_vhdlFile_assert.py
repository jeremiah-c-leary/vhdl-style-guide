import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

lFileAssert = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','assert_statement','assert_test_input.vhd'))
oFileAssert = vhdlFile.vhdlFile(lFileAssert)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','assert_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileAssertMethods(unittest.TestCase):

    def test_isAssertKeyword_assignment(self):
        lExpected = [6,10,15,19,26]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileAssert.lines):
            if oLine.isAssertKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isAssertEnd_assignment(self):
        lExpected = [8,12,17,21,27]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileAssert.lines):
            if oLine.isAssertEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideAssert_assignment(self):
        lExpected = [6,7,8,10,11,12,15,16,17,19,20,21,26,27]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileAssert.lines):
            if oLine.insideAssert:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_indent(self):
        lExpected = [None,1,1,None,2,3,None,1,None]
        lActual = []
        for iIndex, oLine in enumerate(oFileAssert.lines):
            if iIndex > 21 and iIndex < 31:
                lActual.append(oLine.indentLevel)
        self.assertEqual(lActual, lExpected)

    def test_sequential(self):
        lExpected = []
        lActual = []
        for iIndex, oLine in enumerate(oFileAssert.lines):
            if oLine.insideSequential:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_assert_label(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((11,0))
        lExpected.append((14,0))
        lExpected.append((17,0))
        lExpected.append((27,0))
        lExpected.append((35,0))
        lExpected.append((43,0))

        utils.validate_token(self, oFile, lExpected, parser.assert_label)

    def test_assert_label_colon(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((11,2))
        lExpected.append((14,2))
        lExpected.append((18,0))
        lExpected.append((28,0))
        lExpected.append((36,0))
        lExpected.append((43,2))

        utils.validate_token(self, oFile, lExpected, parser.assert_label_colon)

    def test_assert_keyword(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((7,0))
        lExpected.append((11,4))
        lExpected.append((14,4))
        lExpected.append((19,0))
        lExpected.append((29,0))
        lExpected.append((37,0))
        lExpected.append((43,4))

        utils.validate_token(self, oFile, lExpected, parser.assert_keyword)

    def test_assert_condition(self):
        lExpected = []
        lExpected.append((2,6))
        lExpected.append((7,2))
        lExpected.append((11,6))
        lExpected.append((14,6))
        lExpected.append((20,0))
        lExpected.append((30,0))
        lExpected.append((38,0))
        lExpected.append((43,6))

        utils.validate_token(self, oFile, lExpected, parser.assert_condition)

    def test_assert_report_keyword(self):
        lExpected = []
        lExpected.append((3,1))
        lExpected.append((8,1))
        lExpected.append((12,1))
        lExpected.append((21,0))
        lExpected.append((31,0))
        lExpected.append((43,8))

        utils.validate_token(self, oFile, lExpected, parser.assert_report_keyword)

    def test_assert_report_expression(self):
        lExpected = []
        lExpected.append((3,3))
        lExpected.append((8,3))
        lExpected.append((12,3))
        lExpected.append((22,0))
        lExpected.append((32,0))
        lExpected.append((43,10))

        utils.validate_token(self, oFile, lExpected, parser.assert_report_expression)

    def test_assert_severity_keyword(self):
        lExpected = []
        lExpected.append((4,1))
        lExpected.append((9,1))
        lExpected.append((15,1))
        lExpected.append((23,0))
        lExpected.append((39,0))
        lExpected.append((43,12))

        utils.validate_token(self, oFile, lExpected, parser.assert_severity_keyword)

    def test_assert_severity_expression(self):
        lExpected = []
        lExpected.append((4,3))
        lExpected.append((9,3))
        lExpected.append((15,3))
        lExpected.append((24,0))
        lExpected.append((40,0))
        lExpected.append((43,14))

        utils.validate_token(self, oFile, lExpected, parser.assert_severity_expression)

    def test_assert_semicolon(self):
        lExpected = []
        lExpected.append((4,4))
        lExpected.append((9,4))
        lExpected.append((12,4))
        lExpected.append((15,4))
        lExpected.append((25,0))
        lExpected.append((33,0))
        lExpected.append((41,0))
        lExpected.append((43,15))

        utils.validate_token(self, oFile, lExpected, parser.assert_semicolon)


