import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import shared_variable_declaration

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','shared_variable_declaration','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileMethods(unittest.TestCase):

    def test_shared_keyword(self):
        lExpected = []
        lExpected.append((4,0))
        lExpected.append((6,0))
        lExpected.append((8,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.shared_keyword)

    def test_variable_keyword(self):
        lExpected = []
        lExpected.append((4,2))
        lExpected.append((6,2))
        lExpected.append((9,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.variable_keyword)

    def test_variable_identifier(self):
        lExpected = []
        lExpected.append((4,4))

        lExpected.append((6,4))
        lExpected.append((6,7))
        lExpected.append((6,10))

        lExpected.append((10,0))
        lExpected.append((12,0))
        lExpected.append((14,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.identifier)

    def test_variable_comma(self):
        lExpected = []
        lExpected.append((6,5))
        lExpected.append((6,8))
        lExpected.append((11,0))
        lExpected.append((13,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.comma)

    def test_variable_colon(self):
        lExpected = []
        lExpected.append((4,5))

        lExpected.append((6,11))

        lExpected.append((15,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.colon)

    def test_variable_subtype_indication(self):
        lExpected = []
        lExpected.append((4,7))

        lExpected.append((6,13))

        lExpected.append((16,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.subtype_indication)

    def test_variable_assignment_operator(self):
        lExpected = []
        lExpected.append((6,15))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.assignment_operator)

    def test_variable_assignment_expression(self):
        lExpected = []
        lExpected.append((6,17))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.assignment_expression)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((4,8))

        lExpected.append((6,18))

        lExpected.append((17,0))

        utils.validate_token(self, oFile, lExpected, shared_variable_declaration.semicolon)

