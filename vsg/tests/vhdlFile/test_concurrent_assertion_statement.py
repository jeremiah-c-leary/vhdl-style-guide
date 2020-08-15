import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_assertion_statement as token
from vsg.token import assertion


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent_assertion_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

    def test_label_name(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((14,1))
        lExpected.append((17,1))
        lExpected.append((23,1))

        utils.validate_token(self, oFile, lExpected, token.label_name)

    def test_label_colon(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((14,3))
        lExpected.append((17,3))
        lExpected.append((23,3))

        utils.validate_token(self, oFile, lExpected, token.label_colon)

    def test_postponed_keyword(self):
        lExpected = []
        lExpected.append((20,1))
        lExpected.append((23,5))

        utils.validate_token(self, oFile, lExpected, token.postponed_keyword)

    def test_assert_keyword(self):
        lExpected = []
        lExpected.append((6,5))
        lExpected.append((10,1))
        lExpected.append((14,5))
        lExpected.append((17,5))
        lExpected.append((20,3))
        lExpected.append((23,7))

        utils.validate_token(self, oFile, lExpected, assertion.keyword)

    def test_assert_condition(self):
        lExpected = []
        lExpected.append((6,7))
        lExpected.append((10,3))
        lExpected.append((14,7))
        lExpected.append((17,7))
        lExpected.append((20,5))
        lExpected.append((23,9))

        utils.validate_token(self, oFile, lExpected, assertion.condition)

    def test_report_keyword(self):
        lExpected = []
        lExpected.append((7,1))
        lExpected.append((11,1))
        lExpected.append((15,1))
        lExpected.append((21,1))
        lExpected.append((24,1))

        utils.validate_token(self, oFile, lExpected, assertion.report_keyword)

    def test_report_expression(self):
        lExpected = []
        lExpected.append((7,3))
        lExpected.append((11,3))
        lExpected.append((15,3))
        lExpected.append((21,3))
        lExpected.append((24,3))

        utils.validate_token(self, oFile, lExpected, assertion.report_expression)

    def test_severity_expression(self):
        lExpected = []
        lExpected.append((8,3))
        lExpected.append((12,3))
        lExpected.append((18,3))

        utils.validate_token(self, oFile, lExpected, assertion.severity_expression)


#    def test_debug(self):
#        utils.print_objects(oFile, True)
