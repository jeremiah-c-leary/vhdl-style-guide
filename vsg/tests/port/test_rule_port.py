import os

import unittest

from vsg.rules import port
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testRulePortMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = port.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '001')

        dExpected = utils.add_violation_list([25,56])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = port.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([39,56])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = port.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '003')

        dExpected = utils.add_violation_list([25,56])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = port.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '004')

        dExpected = utils.add_violation_list([27,29,43,45,57,59,61])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = port.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '005')

        dExpected = utils.add_violation_list([29,40,42,60])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = port.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '006')

        dExpected = utils.add_violation_list([27,30,44,58])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = port.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '007')

        dExpected = utils.add_violation_list([12,26,29,40,43,57,60,74])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = port.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '008')

        dExpected = utils.add_violation_list([13,30,41,44,61,75])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = port.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '009')

        dExpected = utils.add_violation_list([28,45,59,62])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = port.rule_010()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '010')

        lExpected = []
        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'use_4'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(13)
        dViolation['words_to_fix'] = {'port5'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(14)
        dViolation['words_to_fix'] = {'port6'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(26)
        dViolation['words_to_fix'] = {'i_port1'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(27)
        dViolation['words_to_fix'] = {'o_port2'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['words_to_fix'] = {'io_port3'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(40)
        dViolation['words_to_fix'] = {'i_port1'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(41)
        dViolation['words_to_fix'] = {'o_port2'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(42)
        dViolation['words_to_fix'] = {'io_port3'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(60)
        dViolation['words_to_fix'] = {'port4'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(61)
        dViolation['words_to_fix'] = {'port5'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(62)
        dViolation['words_to_fix'] = {'port6'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(74)
        dViolation['words_to_fix'] = {'port4'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(75)
        dViolation['words_to_fix'] = {'port5'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(76)
        dViolation['words_to_fix'] = {'port6'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_011(self):
        oRule = port.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '011')
        self.assertTrue(oRule.disable)

        dExpected = utils.add_violation_list([12,13,14,29,30,31,43,44,45,60,61,62,74,75,76,99,100,101,152,161,169,170,171,172,173])
        dExpected.extend(utils.add_violation_list(range(181, 186)))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = port.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '012')

        dExpected = utils.add_violation_list([43,58,75])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = port.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '013')

        dExpected = utils.add_violation_list([119,121])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = port.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '014')

        dExpected = utils.add_violation_list([31,62])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = port.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '015')

        dExpected = utils.add_violation_list([46,77])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = port.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [utils.add_violation(140)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = port.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '017')

        lExpected = []
        dViolation = utils.add_violation(25)
        dViolation['words_to_fix'] = {'PORt'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(39)
        dViolation['words_to_fix'] = {'PORt'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(98)
        dViolation['words_to_fix'] = {'Port'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_018(self):
        oRule = port.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '018')

        lExpected = []
        dViolation = utils.add_violation(26)
        dViolation['words_to_fix'] = {'SIGNED'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(27)
        dViolation['words_to_fix'] = {'STD_LOGIC'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['words_to_fix'] = {'NATURAL'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(29)
        dViolation['words_to_fix'] = {'INTEGER'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(31)
        dViolation['words_to_fix'] = {'UNSIGNED'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(44)
        dViolation['words_to_fix'] = {'STD_LOGIC'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_019(self):
        oRule = port.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '019')

        lExpected = []
        dViolation = utils.add_violation(40)
        dViolation['words_to_fix'] = {'IN'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(43)
        dViolation['words_to_fix'] = {'iN'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(44)
        dViolation['words_to_fix'] = {'oUt'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(45)
        dViolation['words_to_fix'] = {'inOut'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_020(self):
        oRule = port.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '020')

        dExpected = [utils.add_violation(141)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = port.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '021')

        dExpected = [utils.add_violation(150)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = port.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '022')

        dExpected = [utils.add_violation(159)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = port.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '023')

        dExpected = utils.add_violation_list([170,171])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = port.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '024')

        lExpected = [utils.add_violation(188)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_025_default(self):
        oRule = port.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '025')
        self.assertTrue(oRule.disable)

        lExpected = utils.add_violation_list([9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131,141,142,152,161,169,170,171,172,173,181,182,183,184,185])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_025_configured(self):
        oRule = port.rule_025()
        oRule.suffixes = ['_OUT']
        lExpected = utils.add_violation_list([9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131,141,142,161,169,170,171,172,173,181,182,183,184,185])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)
