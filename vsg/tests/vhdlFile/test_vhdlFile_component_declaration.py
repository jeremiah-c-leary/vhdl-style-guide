import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import component_declaration as token

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','component_declaration','classification_inside_block_declarative_item_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_block_declarative_item(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((4,1))
        lExpected.append((8,1))
        lExpected.append((12,1))
        lExpected.append((17,1))
        lExpected.append((25,1))
        lExpected.append((33,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)

    def test_identifier(self):
        lExpected = []
        lExpected.append((4,3))
        lExpected.append((8,3))
        lExpected.append((12,3))
        lExpected.append((17,3))
        lExpected.append((25,3))
        lExpected.append((33,3))

        utils.validate_token(self, oFile, lExpected, token.identifier)

    def test_is_keyword(self):
        lExpected = []
        lExpected.append((4,5))
        lExpected.append((17,5))
        lExpected.append((25,5))
        lExpected.append((33,5))

        utils.validate_token(self, oFile, lExpected, token.is_keyword)

    def test_end_keyword(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((10,1))
        lExpected.append((14,1))
        lExpected.append((22,1))
        lExpected.append((30,1))
        lExpected.append((42,1))

        utils.validate_token(self, oFile, lExpected, token.end_keyword)

    def test_end_component_keyword(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((10,3))
        lExpected.append((14,3))
        lExpected.append((22,3))
        lExpected.append((30,3))
        lExpected.append((42,3))

        utils.validate_token(self, oFile, lExpected, token.end_component_keyword)

    def test_simple_name(self):
        lExpected = []
        lExpected.append((6,5))
        lExpected.append((10,5))
        lExpected.append((22,5))
        lExpected.append((30,5))
        lExpected.append((42,5))

        utils.validate_token(self, oFile, lExpected, token.simple_name)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((6,6))
        lExpected.append((10,6))
        lExpected.append((14,4))
        lExpected.append((22,6))
        lExpected.append((30,6))
        lExpected.append((42,6))

        utils.validate_token(self, oFile, lExpected, token.semicolon)

lFile1 = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','component_declaration','classification_inside_package_declarative_item_test_input.vhd'))
oFile1 = vhdlFile.vhdlFile(lFile1)

class test_package_declarative_item(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((4,1))
        lExpected.append((8,1))
        lExpected.append((12,1))
        lExpected.append((17,1))
        lExpected.append((25,1))
        lExpected.append((33,1))

        utils.validate_token(self, oFile1, lExpected, token.keyword)

    def test_identifier(self):
        lExpected = []
        lExpected.append((4,3))
        lExpected.append((8,3))
        lExpected.append((12,3))
        lExpected.append((17,3))
        lExpected.append((25,3))
        lExpected.append((33,3))

        utils.validate_token(self, oFile1, lExpected, token.identifier)

    def test_is_keyword(self):
        lExpected = []
        lExpected.append((4,5))
        lExpected.append((17,5))
        lExpected.append((25,5))
        lExpected.append((33,5))

        utils.validate_token(self, oFile1, lExpected, token.is_keyword)

    def test_end_keyword(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((10,1))
        lExpected.append((14,1))
        lExpected.append((22,1))
        lExpected.append((30,1))
        lExpected.append((42,1))

        utils.validate_token(self, oFile1, lExpected, token.end_keyword)

    def test_end_component_keyword(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((10,3))
        lExpected.append((14,3))
        lExpected.append((22,3))
        lExpected.append((30,3))
        lExpected.append((42,3))

        utils.validate_token(self, oFile1, lExpected, token.end_component_keyword)

    def test_simple_name(self):
        lExpected = []
        lExpected.append((6,5))
        lExpected.append((10,5))
        lExpected.append((22,5))
        lExpected.append((30,5))
        lExpected.append((42,5))

        utils.validate_token(self, oFile1, lExpected, token.simple_name)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((6,6))
        lExpected.append((10,6))
        lExpected.append((14,4))
        lExpected.append((22,6))
        lExpected.append((30,6))
        lExpected.append((42,6))

        utils.validate_token(self, oFile1, lExpected, token.semicolon)

