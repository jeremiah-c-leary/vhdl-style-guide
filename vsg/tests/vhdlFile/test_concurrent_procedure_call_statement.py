import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_procedure_call_statement as token
from vsg.token import procedure_call


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent_procedure_call_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

    def test_label_name(self):
        lExpected = []
        lExpected.append((10,1))
        lExpected.append((11,1))
        lExpected.append((14,1))
        lExpected.append((15,1))

        utils.validate_token(self, oFile, lExpected, token.label_name)

    def test_label_colon(self):
        lExpected = []
        lExpected.append((10,2))
        lExpected.append((11,3))
        lExpected.append((14,2))
        lExpected.append((15,3))

        utils.validate_token(self, oFile, lExpected, token.label_colon)

    def test_postponed_keyword(self):
        lExpected = []
        lExpected.append((14,4))
        lExpected.append((15,5))
        lExpected.append((18,1))
        lExpected.append((19,1))

        utils.validate_token(self, oFile, lExpected, token.postponed_keyword)

    def test_procedure_name(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((7,1))
        lExpected.append((10,4))
        lExpected.append((11,5))
        lExpected.append((14,6))
        lExpected.append((15,7))
        lExpected.append((18,3))
        lExpected.append((19,3))

        utils.validate_token(self, oFile, lExpected, procedure_call.procedure_name)

    def test_open_parenthesis(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((7,3))
        lExpected.append((10,6))
        lExpected.append((11,7))
        lExpected.append((14,8))
        lExpected.append((15,9))
        lExpected.append((18,5))
        lExpected.append((19,5))

        utils.validate_token(self, oFile, lExpected, procedure_call.open_parenthesis)

    def test_close_parenthesis(self):
        lExpected = []
        lExpected.append((6,23))
        lExpected.append((7,16))
        lExpected.append((10,8))
        lExpected.append((12,6))
        lExpected.append((14,10))
        lExpected.append((16,6))
        lExpected.append((18,7))
        lExpected.append((20,6))

        utils.validate_token(self, oFile, lExpected, procedure_call.close_parenthesis)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((6,24))
        lExpected.append((7,17))
        lExpected.append((10,9))
        lExpected.append((12,7))
        lExpected.append((14,11))
        lExpected.append((16,7))
        lExpected.append((18,8))
        lExpected.append((20,7))

        utils.validate_token(self, oFile, lExpected, token.semicolon)


    def test_classification(self):
        sTestDir = os.path.join(os.path.dirname(__file__),'..','concurrent_procedure_call_statement')

        lExpected = []
        utils.read_file(os.path.join(sTestDir, 'classification_results.txt'), lExpected, False)

        lActual = []

        for oObject in utils.extract_objects(oFile, True):
            lActual.append(str(oObject))
        
        self.assertEqual(lExpected, lActual)

    def test_debug(self):
        utils.print_objects(oFile, True)
