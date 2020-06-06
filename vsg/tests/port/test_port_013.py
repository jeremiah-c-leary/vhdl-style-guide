import os

import unittest

from vsg.rules import port
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'port_013_input.vhd'))


class testRulePortMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_013(self):
        oRule = port.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '013')

        dExpected = utils.add_violation_list([5,6])
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = port.rule_013()
        oRule.fix(self.oFile)

        self.assertEqual(self.oFile.lines[5].line, '    I_INPUT : in T_CUSTOM_ARRAY(G_A\'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => \'0\')); -- This should result in two lines')
        self.assertEqual(self.oFile.lines[6].line, '    I_INPUT2 : in T_CUSTOM_ARRAY(G_A\'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => \'0\')); -- This should result in two lines')
        self.assertEqual(self.oFile.lines[7].line, '    I_INPUT : in T_CUSTOM_ARRAY(G_A\'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => \'0\')); -- This should result in three lines')
        self.assertEqual(self.oFile.lines[8].line, '    I_INPUT2 : in T_CUSTOM_ARRAY(G_A\'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => \'0\')); -- This should result in three lines')
        self.assertEqual(self.oFile.lines[9].line, '    I_INPUT3 : in T_CUSTOM_ARRAY(G_A\'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => \'0\')); -- This should result in three lines')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        
