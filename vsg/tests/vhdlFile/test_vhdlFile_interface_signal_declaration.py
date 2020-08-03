import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser
from vsg.token import interface_signal_declaration as token
from vsg.token import interface_list

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','interface_signal_declaration','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((16,1))
        lExpected.append((17,1))
        lExpected.append((18,1))
        lExpected.append((19,1))
        lExpected.append((20,1))
        lExpected.append((21,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)


    def test_identifier(self):
        lExpected = []
        lExpected.append((5,1))
        lExpected.append((6,1))
        lExpected.append((7,1))
        lExpected.append((8,1))
        lExpected.append((9,1))
        lExpected.append((10,1))

        lExpected.append((16,3))
        lExpected.append((17,3))
        lExpected.append((18,3))
        lExpected.append((19,3))
        lExpected.append((20,3))
        lExpected.append((21,3))
        utils.validate_token(self, oFile, lExpected, token.identifier)

    def test_colon(self):
        lExpected = []
        lExpected.append((5,3))
        lExpected.append((6,3))
        lExpected.append((7,3))
        lExpected.append((8,3))
        lExpected.append((9,3))
        lExpected.append((10,3))

        lExpected.append((16,5))
        lExpected.append((17,5))
        lExpected.append((18,5))
        lExpected.append((19,5))
        lExpected.append((20,5))
        lExpected.append((21,5))
        utils.validate_token(self, oFile, lExpected, token.colon)

    def test_mode(self):
        lExpected = []
        lExpected.append((5,5))
        lExpected.append((6,5))
        lExpected.append((7,5))
        lExpected.append((8,5))
        lExpected.append((9,5))

        lExpected.append((16,7))
        lExpected.append((17,7))
        lExpected.append((18,7))
        lExpected.append((19,7))
        lExpected.append((20,7))
        utils.validate_token(self, oFile, lExpected, token.mode_keyword)

    def test_subtype_indication(self):
        lExpected = []
        lExpected.append((5,7))
        lExpected.append((6,7))
        lExpected.append((7,7))
        lExpected.append((8,7))
        lExpected.append((9,7))
        lExpected.append((10,5))

        lExpected.append((16,9))
        lExpected.append((17,9))
        lExpected.append((18,9))
        lExpected.append((19,9))
        lExpected.append((20,9))
        lExpected.append((21,7))
        utils.validate_token(self, oFile, lExpected, token.subtype_indication)

    def test_bus_keyword(self):
        lExpected = []
        lExpected.append((7,9))
        lExpected.append((8,9))

        utils.validate_token(self, oFile, lExpected, token.bus_keyword)

    def test_assignment_operator(self):
        lExpected = []
        lExpected.append((8,11))
        lExpected.append((9,9))

        utils.validate_token(self, oFile, lExpected, token.assignment_operator)

    def test_static_expression(self):
        lExpected = []
        lExpected.append((8,13))
        lExpected.append((9,11))

        utils.validate_token(self, oFile, lExpected, token.static_expression)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((5,8))
        lExpected.append((6,8))
        lExpected.append((7,10))
        lExpected.append((8,14))
        lExpected.append((9,12))

        lExpected.append((16,10))
        lExpected.append((17,10))
        lExpected.append((18,10))
        lExpected.append((19,10))
        lExpected.append((20,10))

        utils.validate_token(self, oFile, lExpected, interface_list.semicolon)

