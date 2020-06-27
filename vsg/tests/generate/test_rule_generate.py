import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generate','generate_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleGenerateMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = generate.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '001')

        dExpected = utils.add_violation_list([11,16,105])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = generate.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '002')

        lExpected = []
        dViolation = utils.add_violation(21)
        dViolation['label'] = 'GENERATE_1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(26)
        dViolation['label'] = 'GENERATE_1'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003(self):
        oRule = generate.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [utils.add_violation(54)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = generate.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [utils.add_violation(56)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_uppercase(self):
        oRule = generate.rule_005()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [{'lines':[{'number': 11}], 'words_to_fix': {'generate_1'}},
                     {'lines':[{'number': 16}], 'words_to_fix': {'generate_1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_lowercase(self):
        oRule = generate.rule_005()

        dExpected = [{'lines':[{'number': 6}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 21}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 26}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 31}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 36}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 41}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 46}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 51}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 56}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 60}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 65}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 68}], 'words_to_fix': {'GENERATE_2'}},
                     {'lines':[{'number': 71}], 'words_to_fix': {'GENERATE_3'}},
                     {'lines':[{'number': 77}], 'words_to_fix': {'GENERATE_4'}},
                     {'lines':[{'number': 83}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 88}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 90}], 'words_to_fix': {'GENERATE_2'}},
                     {'lines':[{'number': 94}], 'words_to_fix': {'GENERATE_3'}},
                     {'lines':[{'number': 104}], 'words_to_fix': {'GENERATE_1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = generate.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '006')

        dExpected = utils.add_violation_list([12,17])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = generate.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '007')

        dExpected = utils.add_violation_list([14,19,106])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = generate.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [utils.add_violation(29)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = generate.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [{'lines':[{'number': 19}], 'words_to_fix': {'END'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_lowercase(self):
        oRule = generate.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [{'lines':[{'number': 19}], 'words_to_fix': {'GENERATE'}},
                     {'lines':[{'number': 62}], 'words_to_fix': {'Generate'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_uppercase(self):
        oRule = generate.rule_010()
        oRule.case = 'upper'

        dExpected = [{'lines':[{'number': 9}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 14}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 24}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 29}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 34}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 39}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 44}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 49}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 54}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 58}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 62}], 'words_to_fix': {'Generate'}},
                     {'lines':[{'number': 73}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 75}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 79}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 86}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 96}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 98}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 100}], 'words_to_fix': {'generate'}},
                     {'lines':[{'number': 106}], 'words_to_fix': {'generate'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_uppercase(self):
        oRule = generate.rule_012()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [{'lines':[{'number': 14}], 'words_to_fix': {'generate_1'}},
                     {'lines':[{'number': 19}], 'words_to_fix': {'generate_1'}},
                     {'lines':[{'number': 73}], 'words_to_fix': {'generate_3'}},
                     {'lines':[{'number': 96}], 'words_to_fix': {'generate_3'}},
                     {'lines':[{'number': 98}], 'words_to_fix': {'generate_2'}},
                     {'lines':[{'number': 100}], 'words_to_fix': {'generate_1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_lowercase(self):
        oRule = generate.rule_012()

        dExpected = [{'lines':[{'number': 9}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 29}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 34}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 39}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 44}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 49}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 54}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 58}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 62}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 75}], 'words_to_fix': {'GENERATE_2'}},
                     {'lines':[{'number': 79}], 'words_to_fix': {'GENERATE_4'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 86}], 'words_to_fix': {'GENERATE_1'}},
                     {'lines':[{'number': 106}], 'words_to_fix': {'GENERATE_1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = generate.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [utils.add_violation(34)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = generate.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '014')

        dExpected = utils.add_violation_list([21,26])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = generate.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [utils.add_violation(104)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017_with_default(self):
        oRule = generate.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '017')
        lExpected = utils.add_violation_list([6,11,16,21,26,31,36,41,46,51,56,
                                              60,65,68,71,77,83,88,90,94,104])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_017_with_override(self):
        oRule = generate.rule_017()
        oRule.prefixes = ['generate_', 'g_']
        lExpected = utils.add_violation_list([])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)
