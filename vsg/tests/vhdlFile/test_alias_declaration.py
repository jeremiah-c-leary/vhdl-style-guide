import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import alias_declaration as token

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','alias_declaration','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_token(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((8,1))
        lExpected.append((10,1))
        lExpected.append((12,1))
        lExpected.append((14,1))
        lExpected.append((16,1))
        lExpected.append((18,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)

    def test_identifier(self):
        lExpected = []
        lExpected.append((8,3))
        lExpected.append((10,3))
        lExpected.append((12,3))
        lExpected.append((14,3))

        utils.validate_token(self, oFile, lExpected, token.identifier)

    def test_character_literal(self):
        lExpected = []
        lExpected.append((16,3))

        utils.validate_token(self, oFile, lExpected, token.character_literal)

    def test_operator_symbol(self):
        lExpected = []
        lExpected.append((18,3))

        utils.validate_token(self, oFile, lExpected, token.operator_symbol)

    def test_colon(self):
        lExpected = []
        lExpected.append((8,5))
        lExpected.append((12,5))

        utils.validate_token(self, oFile, lExpected, token.colon)

    def test_subtype_indication(self):
        lExpected = []
        lExpected.append((8,7))
        lExpected.append((12,7))

        utils.validate_token(self, oFile, lExpected, token.subtype_indication)

    def test_is_keyword(self):
        lExpected = []
        lExpected.append((8,9))
        lExpected.append((10,5))
        lExpected.append((12,9))
        lExpected.append((14,5))
        lExpected.append((16,5))
        lExpected.append((18,5))

        utils.validate_token(self, oFile, lExpected, token.is_keyword)

    def test_name(self):
        lExpected = []
        lExpected.append((8,11))
        lExpected.append((10,7))
        lExpected.append((12,11))
        lExpected.append((14,7))
        lExpected.append((16,7))
        lExpected.append((18,7))

        utils.validate_token(self, oFile, lExpected, token.name)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((8,14))
        lExpected.append((10,10))
        lExpected.append((12,12))
        lExpected.append((14,8))
        lExpected.append((16,8))
        lExpected.append((18,8))

        utils.validate_token(self, oFile, lExpected, token.semicolon)

