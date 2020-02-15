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

        dExpected = [25,56]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = port.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [39,56]
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

        dExpected = [27,29,43,45,57,59,61]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = port.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [29,40,42,60]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = port.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [27,30,44,58]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = port.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [12,26,29,40,43,57,60,74]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = port.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [13,30,41,44,61,75]
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
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [{'line_number': 12, 'words_to_fix': {'use_4'}},
                     {'line_number': 13, 'words_to_fix': {'port5'}},
                     {'line_number': 14, 'words_to_fix': {'port6'}},
                     {'line_number': 26, 'words_to_fix': {'i_port1'}},
                     {'line_number': 27, 'words_to_fix': {'o_port2'}},
                     {'line_number': 28, 'words_to_fix': {'io_port3'}},
                     {'line_number': 40, 'words_to_fix': {'i_port1'}},
                     {'line_number': 41, 'words_to_fix': {'o_port2'}},
                     {'line_number': 42, 'words_to_fix': {'io_port3'}},
                     {'line_number': 60, 'words_to_fix': {'port4'}},
                     {'line_number': 61, 'words_to_fix': {'port5'}},
                     {'line_number': 62, 'words_to_fix': {'port6'}},
                     {'line_number': 74, 'words_to_fix': {'port4'}},
                     {'line_number': 75, 'words_to_fix': {'port5'}},
                     {'line_number': 76, 'words_to_fix': {'port6'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

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

        dExpected = [43,58,75]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = port.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [119,121]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = port.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '014')

        dExpected = [31,62]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = port.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [46,77]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = port.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [140]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = port.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [{'line_number': 25, 'words_to_fix': {'PORt'}},
                     {'line_number': 39, 'words_to_fix': {'PORt'}},
                     {'line_number': 98, 'words_to_fix': {'Port'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = port.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '018')

        dExpected = [{'line_number': 26, 'words_to_fix': {'SIGNED'}},
                     {'line_number': 27, 'words_to_fix': {'STD_LOGIC'}},
                     {'line_number': 28, 'words_to_fix': {'NATURAL'}},
                     {'line_number': 29, 'words_to_fix': {'INTEGER'}},
                     {'line_number': 30, 'words_to_fix': {'STD_LOGIC_VECTOR'}},
                     {'line_number': 31, 'words_to_fix': {'UNSIGNED'}},
                     {'line_number': 44, 'words_to_fix': {'STD_LOGIC'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = port.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '019')

        dExpected = [{'line_number': 40, 'words_to_fix': {'IN'}},
                     {'line_number': 43, 'words_to_fix': {'iN'}},
                     {'line_number': 44, 'words_to_fix': {'oUt'}},
                     {'line_number': 45, 'words_to_fix': {'inOut'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = port.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '020')

        dExpected = [141]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = port.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '021')

        dExpected = [150]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = port.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '022')

        dExpected = [159]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = port.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '023')

        dExpected = [170,171]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = port.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '024')

        lExpected = [188]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_025_default(self):
        oRule = port.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '025')
        self.assertTrue(oRule.disable)

        dExpected = [{'lineNumber': 9},
                     {'lineNumber': 10},
                     {'lineNumber': 11},
                     {'lineNumber': 12},
                     {'lineNumber': 13},
                     {'lineNumber': 14},
                     {'lineNumber': 26},
                     {'lineNumber': 27},
                     {'lineNumber': 28},
                     {'lineNumber': 29},
                     {'lineNumber': 30},
                     {'lineNumber': 31},
                     {'lineNumber': 40},
                     {'lineNumber': 41},
                     {'lineNumber': 42},
                     {'lineNumber': 43},
                     {'lineNumber': 44},
                     {'lineNumber': 45},
                     {'lineNumber': 57},
                     {'lineNumber': 58},
                     {'lineNumber': 59},
                     {'lineNumber': 60},
                     {'lineNumber': 61},
                     {'lineNumber': 62},
                     {'lineNumber': 71},
                     {'lineNumber': 72},
                     {'lineNumber': 73},
                     {'lineNumber': 74},
                     {'lineNumber': 75},
                     {'lineNumber': 76},
                     {'lineNumber': 87},
                     {'lineNumber': 88},
                     {'lineNumber': 89},
                     {'lineNumber': 119},
                     {'lineNumber': 120},
                     {'lineNumber': 121},
                     {'lineNumber': 129},
                     {'lineNumber': 130},
                     {'lineNumber': 131},
                     {'lineNumber': 141},
                     {'lineNumber': 142},
                     {'lineNumber': 152},
                     {'lineNumber': 161},
                     {'lineNumber': 169},
                     {'lineNumber': 170},
                     {'lineNumber': 171},
                     {'lineNumber': 172},
                     {'lineNumber': 173},
                     {'lineNumber': 181},
                     {'lineNumber': 182},
                     {'lineNumber': 183},
                     {'lineNumber': 184},
                     {'lineNumber': 185}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025_configured(self):
        oRule = port.rule_025()
        oRule.suffixes = ['_OUT']

        dExpected = [{'lineNumber': 9},
                     {'lineNumber': 10},
                     {'lineNumber': 11},
                     {'lineNumber': 12},
                     {'lineNumber': 13},
                     {'lineNumber': 14},
                     {'lineNumber': 26},
                     {'lineNumber': 27},
                     {'lineNumber': 28},
                     {'lineNumber': 29},
                     {'lineNumber': 30},
                     {'lineNumber': 31},
                     {'lineNumber': 40},
                     {'lineNumber': 41},
                     {'lineNumber': 42},
                     {'lineNumber': 43},
                     {'lineNumber': 44},
                     {'lineNumber': 45},
                     {'lineNumber': 57},
                     {'lineNumber': 58},
                     {'lineNumber': 59},
                     {'lineNumber': 60},
                     {'lineNumber': 61},
                     {'lineNumber': 62},
                     {'lineNumber': 71},
                     {'lineNumber': 72},
                     {'lineNumber': 73},
                     {'lineNumber': 74},
                     {'lineNumber': 75},
                     {'lineNumber': 76},
                     {'lineNumber': 87},
                     {'lineNumber': 88},
                     {'lineNumber': 89},
                     {'lineNumber': 99},
                     {'lineNumber': 100},
                     {'lineNumber': 101},
                     {'lineNumber': 119},
                     {'lineNumber': 120},
                     {'lineNumber': 121},
                     {'lineNumber': 129},
                     {'lineNumber': 130},
                     {'lineNumber': 131},
                     {'lineNumber': 141},
                     {'lineNumber': 142},
                     {'lineNumber': 161},
                     {'lineNumber': 169},
                     {'lineNumber': 170},
                     {'lineNumber': 171},
                     {'lineNumber': 172},
                     {'lineNumber': 173},
                     {'lineNumber': 181},
                     {'lineNumber': 182},
                     {'lineNumber': 183},
                     {'lineNumber': 184},
                     {'lineNumber': 185}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
