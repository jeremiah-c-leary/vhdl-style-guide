import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_simple_signal_assignment as token


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent_simple_signal_assignment','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_token(unittest.TestCase):

    def test_target(self):
        lExpected = []
        lExpected.append((7,1))
        lExpected.append((10,1))
        lExpected.append((13,1))
        lExpected.append((16,1))
        lExpected.append((19,1))
        lExpected.append((22,1))
        lExpected.append((25,1))
        lExpected.append((28,1))

        utils.validate_token(self, oFile, lExpected, token.target)

    def test_assignment(self):
        lExpected = []
        lExpected.append((7,3))
        lExpected.append((10,3))
        lExpected.append((13,3))
        lExpected.append((16,3))
        lExpected.append((19,3))
        lExpected.append((22,3))
        lExpected.append((25,3))
        lExpected.append((28,3))

        utils.validate_token(self, oFile, lExpected, token.assignment)

    def test_guarded_keyword(self):
        lExpected = []
        lExpected.append((10,5))
        lExpected.append((22,5))
        lExpected.append((25,5))
        lExpected.append((28,5))

        utils.validate_token(self, oFile, lExpected, token.guarded_keyword)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((7,6))
        lExpected.append((10,8))
        lExpected.append((13,8))
        lExpected.append((16,8))
        lExpected.append((19,14))
        lExpected.append((22,10))
        lExpected.append((25,10))
        lExpected.append((28,16))

        utils.validate_token(self, oFile, lExpected, token.semicolon)

#    def test_debug(self):
#        utils.print_objects(oFile, True)
