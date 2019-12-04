import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'concurrent_parenthesis_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleConcurrentWithParenthesis(unittest.TestCase):

    def test_rule_003(self):
        oRule = concurrent.rule_003()
        dExpected = [22,25,29,32]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
