import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_selected_signal_assignment as token
from vsg.token import selected_waveforms


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent_selected_signal_assignment','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

    def test_with_keyword(self):
        lExpected = []
        lExpected.append((7,1))
        lExpected.append((15,1))
        lExpected.append((23,1))
        lExpected.append((30,1))
        lExpected.append((37,1))

        utils.validate_token(self, oFile, lExpected, token.with_keyword)

    def test_select_keyword(self):
        lExpected = []
        lExpected.append((7,5))
        lExpected.append((15,5))
        lExpected.append((23,5))
        lExpected.append((30,5))
        lExpected.append((37,5))

        utils.validate_token(self, oFile, lExpected, token.select_keyword)

    def test_target(self):
        lExpected = []
        lExpected.append((8,1))
        lExpected.append((16,1))
        lExpected.append((24,1))
        lExpected.append((31,1))
        lExpected.append((38,1))

        utils.validate_token(self, oFile, lExpected, token.target)

    def test_assignment(self):
        lExpected = []
        lExpected.append((8,3))
        lExpected.append((16,3))
        lExpected.append((24,3))
        lExpected.append((31,3))
        lExpected.append((38,3))

        utils.validate_token(self, oFile, lExpected, token.assignment)

    def test_guarded_keyword(self):
        lExpected = []
        lExpected.append((16,5))

        utils.validate_token(self, oFile, lExpected, token.guarded_keyword)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((11,6))
        lExpected.append((19,6))
        lExpected.append((27,6))
        lExpected.append((34,6))
        lExpected.append((41,6))

        utils.validate_token(self, oFile, lExpected, token.semicolon)

#    def test_debug(self):
#        utils.print_objects(oFile, True)
