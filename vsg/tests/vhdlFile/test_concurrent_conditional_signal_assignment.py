import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_conditional_signal_assignment as token
from vsg.token import conditional_waveforms


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent_conditional_signal_assignment','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_token(unittest.TestCase):

    def test_target(self):
        lExpected = []
        lExpected.append((7,1))
        lExpected.append((12,1))
        lExpected.append((17,1))
        lExpected.append((22,1))
        lExpected.append((27,1))
        lExpected.append((32,1))
        lExpected.append((37,1))
        lExpected.append((42,1))
        lExpected.append((47,1))
        lExpected.append((49,1))

        utils.validate_token(self, oFile, lExpected, token.target)

    def test_assignment(self):
        lExpected = []
        lExpected.append((7,3))
        lExpected.append((12,3))
        lExpected.append((17,3))
        lExpected.append((22,3))
        lExpected.append((27,3))
        lExpected.append((32,3))
        lExpected.append((37,3))
        lExpected.append((42,3))
        lExpected.append((47,3))
        lExpected.append((49,3))

        utils.validate_token(self, oFile, lExpected, token.assignment)

    def test_guarded_keyword(self):
        lExpected = []
        lExpected.append((12,5))
        lExpected.append((32,5))
        lExpected.append((37,5))
        lExpected.append((42,5))

        utils.validate_token(self, oFile, lExpected, token.guarded_keyword)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((9,2))
        lExpected.append((14,2))
        lExpected.append((19,2))
        lExpected.append((24,2))
        lExpected.append((29,2))
        lExpected.append((34,2))
        lExpected.append((39,2))
        lExpected.append((44,2))
        lExpected.append((47,14))
        lExpected.append((49,22))

        utils.validate_token(self, oFile, lExpected, token.semicolon)

#    def test_debug(self):
#        utils.print_objects(oFile, True)
