import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_signal_assignment_statement as token


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent_signal_assignment_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

    def test_label_name(self):
        lExpected = []
        lExpected.append((26,1))
        lExpected.append((29,1))
        lExpected.append((34,1))
        lExpected.append((45,1))
        lExpected.append((48,1))
        lExpected.append((53,1))

        utils.validate_token(self, oFile, lExpected, token.label_name)

    def test_label_colon(self):
        lExpected = []
        lExpected.append((26,3))
        lExpected.append((29,3))
        lExpected.append((34,3))
        lExpected.append((45,3))
        lExpected.append((48,3))
        lExpected.append((53,3))

        utils.validate_token(self, oFile, lExpected, token.label_colon)

    def test_postponed_keyword(self):
        lExpected = []
        lExpected.append((45,5))
        lExpected.append((48,5))
        lExpected.append((53,5))
        lExpected.append((64,1))
        lExpected.append((67,1))
        lExpected.append((72,1))

        utils.validate_token(self, oFile, lExpected, token.postponed_keyword)

#    def test_debug(self):
#        utils.print_objects(oFile, True)
