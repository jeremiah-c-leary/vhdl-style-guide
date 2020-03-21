import os

import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generic_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileMultiple = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generic_multiple_on_one_line_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(lFileMultiple)
lFileComponent = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generic_component_test_input.vhd'))
oFileComponent = vhdlFile.vhdlFile(lFileComponent)

class testRuleGenericMethods(unittest.TestCase):


    def test_rule_001(self):
        oRule = generic.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [utils.add_violation(82)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = generic.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([51,66])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = generic.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '003')

        dExpected = utils.add_violation_list([51,82])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = generic.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '004')

        dExpected = utils.add_violation_list([21,53,68,83])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = generic.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '005')

        dExpected = utils.add_violation_list([36,37,52,67,84])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = generic.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '006')

        dExpected = utils.add_violation_list([37,52,53,68,83])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_component_rule_006(self):
        oRule = generic.rule_006()

        dExpected = utils.add_violation_list([36,37])
        oRule.analyze(oFileComponent)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = generic.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [{'line_number': 22, 'words_to_fix': {'G_generic2'}},
                     {'line_number': 36, 'words_to_fix': {'g_generIC1'}},
                     {'line_number': 37, 'words_to_fix': {'G_GeneRIC2'}},
                     {'line_number': 67, 'words_to_fix': {'A_generic1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = generic.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '008')

        dExpected = utils.add_violation_list([85,117])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = generic.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [{'line_number': 66, 'words_to_fix': {'geneRIC'}},
                     {'line_number': 82, 'words_to_fix': {'gENEric'}},
                     {'line_number': 95, 'words_to_fix': {'Generic'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = generic.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [utils.add_violation(97)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = generic.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [utils.add_violation(139)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = generic.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '014')

        dExpected = utils.add_violation_list([68,116])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = generic.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [utils.add_violation(21)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

        oRule.violations = []
        dExpected = [utils.add_violation(5)]
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = generic.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [{'line_number': 52, 'words_to_fix': {'STD_LOGIC'}},
                     {'line_number': 96, 'words_to_fix': {'STD_LOGIC'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = generic.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '019')

        dExpected = [utils.add_violation(174)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_with_default(self):
        oRule = generic.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '020')

        dExpected = utils.add_violation_list([67,96,116])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_with_2_overrides(self):
        oRule = generic.rule_020()
        oRule.prefixes = ['G_', 'A_']

        dExpected = []
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_with_override(self):
        oRule = generic.rule_020()
        oRule.prefixes = ['A_']

        dExpected = utils.add_violation_list([5,6,21,22,36,37,52,53,68,83,84,97,139,140,155,156,170,171])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
