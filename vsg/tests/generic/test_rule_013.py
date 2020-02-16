import os

import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generic','generic_test_input_rule_013.vhd'))


class testRulePortMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_016(self):
        oRule = generic.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [utils.add_violation(3)]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)


    def test_fix_rule_016(self):
        oRule = generic.rule_013()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[3].line, '  generic  (')
        self.assertEqual(self.oFile.lines[4].line, '    G_GEN_1 : std_logic_vector(6 downto 0);')
        self.assertEqual(self.oFile.lines[5].line, '    G_GEN_2 : std_logic_vector(8 downto 1)')
        self.assertEqual(self.oFile.lines[3].indentLevel + 1, self.oFile.lines[4].indentLevel)

