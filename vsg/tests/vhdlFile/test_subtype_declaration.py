import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import subtype_declaration as token

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','subtype_declaration','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_token(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((5,1))
        lExpected.append((8,1))
        lExpected.append((11,1))
        lExpected.append((14,1))
        lExpected.append((17,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)

    def test_identifier(self):
        lExpected = []
        lExpected.append((5,3))
        lExpected.append((8,3))
        lExpected.append((11,3))
        lExpected.append((14,3))
        lExpected.append((17,3))

        utils.validate_token(self, oFile, lExpected, token.identifier)

    def test_is_keyword(self):
        lExpected = []
        lExpected.append((5,5))
        lExpected.append((8,5))
        lExpected.append((11,5))
        lExpected.append((14,5))
        lExpected.append((17,5))

        utils.validate_token(self, oFile, lExpected, token.is_keyword)

    def test_subtype_indication(self):
        lExpected = []
        lExpected.append((5,7))
        lExpected.append((5,9))
        lExpected.append((5,11))
        lExpected.append((5,13))
        lExpected.append((5,15))

        lExpected.append((8,7))
        lExpected.append((8,9))

        lExpected.append((11,7))
        lExpected.append((11,9))

        lExpected.append((14,7))
        lExpected.append((14,9))
        lExpected.append((14,11))
        lExpected.append((14,13))
        lExpected.append((14,15))

        lExpected.append((17,7))
        lExpected.append((17,8))
        lExpected.append((17,9))
        lExpected.append((17,11))
        lExpected.append((17,13))
        lExpected.append((17,14))

        utils.validate_token(self, oFile, lExpected, token.subtype_indication)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((5,16))
        lExpected.append((8,10))
        lExpected.append((11,10))
        lExpected.append((14,16))
        lExpected.append((17,15))

        utils.validate_token(self, oFile, lExpected, token.semicolon)
