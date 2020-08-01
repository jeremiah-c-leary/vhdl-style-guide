import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

lFileVariable = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))
oFileVariable = vhdlFile.vhdlFile(lFileVariable)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileMethods(unittest.TestCase):

    def test_isVariable_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,27,28,29,37,38,39,47,48,49,57]
        lExpected.extend([66,71])
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileVariable.lines):
            if oLine.isVariable:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_shared_keyword(self):
        lExpected = []
        lExpected.append((9,0))
        lExpected.append((11,0))
        lExpected.append((15,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_shared_keyword)

    def test_variable_keyword(self):
        lExpected = []
        lExpected.append((3,0))
        lExpected.append((5,0))
        lExpected.append((7,0))
        lExpected.append((9,2))
        lExpected.append((11,2))
        lExpected.append((13,0))
        lExpected.append((16,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_keyword)

    def test_variable_identifier(self):
        lExpected = []
        lExpected.append((3,2))
        lExpected.append((5,2))
        lExpected.append((7,2))
        lExpected.append((9,4))
        lExpected.append((11,4))
        lExpected.append((11,7))
        lExpected.append((11,10))
        lExpected.append((13,2))
        lExpected.append((17,0))
        lExpected.append((19,0))
        lExpected.append((21,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_identifier)

    def test_variable_comma(self):
        lExpected = []
        lExpected.append((11,5))
        lExpected.append((11,8))
        lExpected.append((18,0))
        lExpected.append((20,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_comma)

    def test_variable_colon(self):
        lExpected = []
        lExpected.append((3,3))
        lExpected.append((5,3))
        lExpected.append((7,3))
        lExpected.append((9,5))
        lExpected.append((11,11))
        lExpected.append((13,3))
        lExpected.append((22,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_colon)

    def test_variable_subtype_indication(self):
        lExpected = []
        lExpected.append((3,5))
        lExpected.append((3,7))
        lExpected.append((3,9))
        lExpected.append((3,11))
        lExpected.append((3,13))
        lExpected.append((5,5))
        lExpected.append((7,5))
        lExpected.append((7,7))
        lExpected.append((7,8))
        lExpected.append((7,10))
        lExpected.append((7,12))
        lExpected.append((7,13))
        lExpected.append((7,15))
        lExpected.append((7,17))
        lExpected.append((7,19))
        lExpected.append((7,20))
        lExpected.append((9,7))
        lExpected.append((11,13))
        lExpected.append((13,5))
        lExpected.append((23,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_subtype_indication)

    def test_variable_assignment_operator(self):
        lExpected = []
        lExpected.append((3,15))
        lExpected.append((13,7))

        utils.validate_token(self, oFile, lExpected, parser.variable_assignment_operator)

    def test_variable_assignment_expression(self):
        lExpected = []
        lExpected.append((3,17))
        lExpected.append((13,9))

        utils.validate_token(self, oFile, lExpected, parser.variable_assignment_expression)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((3,18))
        lExpected.append((5,6))
        lExpected.append((7,21))
        lExpected.append((9,8))
        lExpected.append((11,14))
        lExpected.append((13,10))
        lExpected.append((24,0))

        utils.validate_token(self, oFile, lExpected, parser.variable_semicolon)

