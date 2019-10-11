import os

import unittest

from vsg.rules import port
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input_2.vhd'))


class testRulePortMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
    
    def test_rule_016(self):
        oRule = port.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [3]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)


    def test_fix_rule_016(self):
        oRule = port.rule_016()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[3].line, '  port  (')
        self.assertEqual(self.oFile.lines[4].line, '    PORT_1 : in std_logic_vector(12 downto 0),')
        self.assertEqual(self.oFile.lines[5].line, '    PORT_2 : out std_logic_vector(0 to 25)')
        self.assertEqual(self.oFile.lines[3].indentLevel + 1, self.oFile.lines[4].indentLevel)

