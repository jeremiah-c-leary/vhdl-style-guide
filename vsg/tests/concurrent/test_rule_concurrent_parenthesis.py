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
        dExpected = [32,35,39,42,45,46,49,50,51,52,55,56]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = concurrent.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[32].line, '            \'1\';')
        self.assertEqual(self.oFile.lines[35].line, '                        (I_CRUFT = \'1\')) else')
        self.assertEqual(self.oFile.lines[39].line, '             0 => q_foo(31 downto  0));')
        self.assertEqual(self.oFile.lines[42].line, '                   unsigned(I_BAR), q_foo\'length);')
        self.assertEqual(self.oFile.lines[45].line, '                                       I_CRUFT = 1) or')
        self.assertEqual(self.oFile.lines[46].line, '                         I_BLAH = 10));')

        self.assertEqual(self.oFile.lines[49].line, '                                       (I_CRUFT = 1 or I_BLAH = 10)')
        self.assertEqual(self.oFile.lines[50].line, '                                       and I_GRUB = 20) or')
        self.assertEqual(self.oFile.lines[51].line, '                                      I_STUB = 45)')
        self.assertEqual(self.oFile.lines[52].line, '                        and I_HUB = 23);')

        self.assertEqual(self.oFile.lines[55].line, '                                       (I_CRUFT = 1 or')
        self.assertEqual(self.oFile.lines[56].line, '                                        I_BLAH = 10)')
        self.assertEqual(self.oFile.lines[57].line, '                                       and I_GRUB = 20) or')
        self.assertEqual(self.oFile.lines[58].line, '                                      I_STUB = 45)')
        self.assertEqual(self.oFile.lines[59].line, '                        and I_HUB = 23);')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

