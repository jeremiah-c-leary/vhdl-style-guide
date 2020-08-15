import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import process_statement as token
from vsg.token import procedure_call


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

    def test_label_name(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((12,1))
        lExpected.append((18,1))
        lExpected.append((22,1))
        lExpected.append((26,1))

        utils.validate_token(self, oFile, lExpected, token.label_name)

    def test_label_colon(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((12,3))
        lExpected.append((18,3))
        lExpected.append((22,3))
        lExpected.append((26,3))

        utils.validate_token(self, oFile, lExpected, token.label_colon)

    def test_postponed_keyword(self):
        lExpected = []
        lExpected.append((12,5))
        lExpected.append((18,5))
        lExpected.append((22,5))

        utils.validate_token(self, oFile, lExpected, token.postponed_keyword)

    def test_keyword(self):
        lExpected = []
        lExpected.append((6,5))
        lExpected.append((12,7))
        lExpected.append((18,7))
        lExpected.append((22,7))
        lExpected.append((26,5))
        lExpected.append((30,1))
        lExpected.append((34,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)

    def test_open_parenthesis(self):
        lExpected = []
        lExpected.append((6,6))
        lExpected.append((12,8))

        utils.validate_token(self, oFile, lExpected, token.open_parenthesis)

    def test_close_parenthesis(self):
        lExpected = []
        lExpected.append((6,14))
        lExpected.append((12,16))

        utils.validate_token(self, oFile, lExpected, token.close_parenthesis)

    def test_begin_keyword(self):
        lExpected = []
        lExpected.append((8,1))
        lExpected.append((14,1))
        lExpected.append((19,1))
        lExpected.append((23,1))
        lExpected.append((27,1))
        lExpected.append((31,1))
        lExpected.append((35,1))

        utils.validate_token(self, oFile, lExpected, token.begin_keyword)

    def test_end_keyword(self):
        lExpected = []
        lExpected.append((10,1))
        lExpected.append((16,1))
        lExpected.append((20,1))
        lExpected.append((24,1))
        lExpected.append((28,1))
        lExpected.append((32,1))
        lExpected.append((36,1))

        utils.validate_token(self, oFile, lExpected, token.end_keyword)

    def test_end_postponed_keyword(self):
        lExpected = []
        lExpected.append((16,3))
        lExpected.append((20,3))
        lExpected.append((24,3))

        utils.validate_token(self, oFile, lExpected, token.end_postponed_keyword)

    def test_end_process_keyword(self):
        lExpected = []
        lExpected.append((10,3))
        lExpected.append((16,5))
        lExpected.append((20,5))
        lExpected.append((24,5))
        lExpected.append((28,3))
        lExpected.append((32,3))
        lExpected.append((36,3))

        utils.validate_token(self, oFile, lExpected, token.end_process_keyword)

    def test_end_process_label_name(self):
        lExpected = []
        lExpected.append((10,5))
        lExpected.append((16,7))
        lExpected.append((20,7))
        lExpected.append((24,7))
        lExpected.append((28,5))

        utils.validate_token(self, oFile, lExpected, token.end_process_label_name)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((10,6))
        lExpected.append((16,8))
        lExpected.append((20,8))
        lExpected.append((24,8))
        lExpected.append((28,6))
        lExpected.append((32,4))
        lExpected.append((36,4))

        utils.validate_token(self, oFile, lExpected, token.semicolon)


#    def test_debug(self):
#        utils.print_objects(oFile, True)
