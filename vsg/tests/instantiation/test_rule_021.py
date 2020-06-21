import os

import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_rule_021_test_input.vhd'))

class testRuleMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_021(self):
        oRule = instantiation.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '021')

        dExpected = [8,13,19,29,32]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)


    def test_fix_rule_021(self):
        oRule = instantiation.rule_021()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[8].line,'      PORT_1 => w_port_1(3 downto 0)  ,')
        self.assertFalse(self.oFile.lines[8].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[9].line,' PORT_2 => w_port_2,')
        self.assertFalse(self.oFile.lines[9].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[10].line,' PORT_3 => w_port_3')
        self.assertFalse(self.oFile.lines[10].isInstantiationPortEnd)

        self.assertEqual(self.oFile.lines[15].line,'      PORT_1 => w_port_1,')
        self.assertFalse(self.oFile.lines[15].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[16].line,' PORT_2 => w_port_2,')
        self.assertFalse(self.oFile.lines[16].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[17].line,'      PORT_3 => w_port_3,')
        self.assertFalse(self.oFile.lines[17].isInstantiationPortEnd)

        self.assertEqual(self.oFile.lines[22].line,'    port map (PORT_1 => w_port_1,')
        self.assertFalse(self.oFile.lines[22].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[23].line,' PORT_2 => w_port_2,')
        self.assertFalse(self.oFile.lines[23].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[24].line,' PORT_3 => w_port3);')
        self.assertTrue(self.oFile.lines[24].isInstantiationPortEnd)

        self.assertEqual(self.oFile.lines[34].line,'    port map (PORT_1 => w_port_1,')
        self.assertFalse(self.oFile.lines[34].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[35].line,' PORT_2 => w_port_2,')
        self.assertFalse(self.oFile.lines[35].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[36].line,' PORT_3 => w_port3(45));')
        self.assertTrue(self.oFile.lines[36].isInstantiationPortEnd)

        self.assertEqual(self.oFile.lines[39].line,'    port map (PORT_1 => w_port_1,')
        self.assertFalse(self.oFile.lines[39].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[40].line,' PORT_2 => w_port_2,')
        self.assertFalse(self.oFile.lines[40].isInstantiationPortEnd)
        self.assertEqual(self.oFile.lines[41].line,' PORT_3 => w_port3(45)')
        self.assertFalse(self.oFile.lines[41].isInstantiationPortEnd)

        self.assertEqual(oRule.violations, [])
