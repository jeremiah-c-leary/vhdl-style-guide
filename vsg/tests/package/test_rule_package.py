import os

import unittest

from vsg.rules import package
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','package','package_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRulePackageMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = package.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [utils.add_violation(32)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = package.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([32,47])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = package.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [utils.add_violation(32)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = package.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '004')

        lExpected = []
        dViolation = utils.add_violation(18)
        dViolation['words_to_fix'] = {'PACKAGE'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = package.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '005')

        dExpected = utils.add_violation_list([18,60])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = package.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '006')

        lExpected = []
        dViolation = utils.add_violation(45)
        dViolation['words_to_fix'] = {'END'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_007(self):
        oRule = package.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [utils.add_violation(58)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = package.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '008')
        lExpected = [{'lines':[{'number': 15}], 'words_to_fix': {'PACK'}},
                     {'lines':[{'number': 45}], 'words_to_fix': {'PACK'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_009(self):
        oRule = package.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '009')
        dExpected = utils.add_violation_list([15,31,58,73])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = package.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '010')
        lExpected = [{'lines':[{'number': 2}], 'words_to_fix': {'PACK'}},
                     {'lines':[{'number': 18}], 'words_to_fix': {'PACK'}},
                     {'lines':[{'number': 32}], 'words_to_fix': {'PACK'}},
                     {'lines':[{'number': 60}], 'words_to_fix': {'PACK'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_011(self):
        oRule = package.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '011')
        dExpected = utils.add_violation_list([47, 60])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = package.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [utils.add_violation(58)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = package.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '013')
        lExpected = []
        dViolation = utils.add_violation(32)
        dViolation['words_to_fix'] = {'IS'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_014(self):
        oRule = package.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '014')
        dExpected = [utils.add_violation(73)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = package.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [utils.add_violation(45)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = package.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '016')

        dExpected = utils.add_violation_list([2, 18, 32, 47, 60, 81])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = package.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '017')

        dExpected = utils.add_violation_list([2, 18, 32, 47, 60, 75])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = package.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '018')

        lExpected = []
        dViolation = utils.add_violation(31)
        dViolation['words_to_fix'] = {'PACKAGE'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)
