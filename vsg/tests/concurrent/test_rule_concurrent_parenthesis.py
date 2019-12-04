import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'concurrent_parenthesis_test_input.vhd'))

class testRuleConcurrentWithParenthesis(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_003(self):
        oRule = concurrent.rule_003()
        dExpected = [22,25,29,32]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = concurrent.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[22].line, '            \'1\';')
        self.assertEqual(self.oFile.lines[25].line, '                        (I_CRUFT = \'1\')) else')
        self.assertEqual(self.oFile.lines[29].line, '             0 => q_foo(31 downto  0));')
        self.assertEqual(self.oFile.lines[32].line, '                   unsigned(I_BAR), q_foo\'length);')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

