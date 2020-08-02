import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser
from vsg.token import port_clause


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','port_clause','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((6,0))
        lExpected.append((12,0))

        utils.validate_token(self, oFile, lExpected, port_clause.keyword)

    def test_open_parenthesis(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((6,2))
        lExpected.append((13,0))

        utils.validate_token(self, oFile, lExpected, port_clause.open_parenthesis)

    def test_close_parenthesis(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((8,0))
        lExpected.append((14,0))

        utils.validate_token(self, oFile, lExpected, port_clause.close_parenthesis)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((2,5))
        lExpected.append((8,1))
        lExpected.append((15,0))

        utils.validate_token(self, oFile, lExpected, port_clause.semicolon)

