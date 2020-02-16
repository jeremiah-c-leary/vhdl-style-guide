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

        dExpected = [21,26]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

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
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [{'line_number': 11, 'words_to_fix': {'generate_1'}},
                     {'line_number': 16, 'words_to_fix': {'generate_1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_lowercase(self):
        oRule = generate.rule_005()
        oRule.case = 'lower'

        dExpected = [{'line_number': 6, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 21, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 26, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 31, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 36, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 41, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 46, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 51, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 56, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 60, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 65, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 68, 'words_to_fix': {'GENERATE_2'}},
                     {'line_number': 71, 'words_to_fix': {'GENERATE_3'}},
                     {'line_number': 77, 'words_to_fix': {'GENERATE_4'}},
                     {'line_number': 83, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 88, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 90, 'words_to_fix': {'GENERATE_2'}},
                     {'line_number': 94, 'words_to_fix': {'GENERATE_3'}},
                     {'line_number': 104, 'words_to_fix': {'GENERATE_1'}}]
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

        dExpected = [{'line_number': 19, 'words_to_fix': {'END'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_lowercase(self):
        oRule = generate.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [{'line_number': 19, 'words_to_fix': {'GENERATE'}},
                     {'line_number': 62, 'words_to_fix': {'Generate'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_uppercase(self):
        oRule = generate.rule_010()
        oRule.case = 'upper'

        dExpected = [{'line_number': 9, 'words_to_fix': {'generate'}},
                     {'line_number': 14, 'words_to_fix': {'generate'}},
                     {'line_number': 24, 'words_to_fix': {'generate'}},
                     {'line_number': 29, 'words_to_fix': {'generate'}},
                     {'line_number': 34, 'words_to_fix': {'generate'}},
                     {'line_number': 39, 'words_to_fix': {'generate'}},
                     {'line_number': 44, 'words_to_fix': {'generate'}},
                     {'line_number': 49, 'words_to_fix': {'generate'}},
                     {'line_number': 54, 'words_to_fix': {'generate'}},
                     {'line_number': 58, 'words_to_fix': {'generate'}},
                     {'line_number': 62, 'words_to_fix': {'Generate'}},
                     {'line_number': 73, 'words_to_fix': {'generate'}},
                     {'line_number': 75, 'words_to_fix': {'generate'}},
                     {'line_number': 79, 'words_to_fix': {'generate'}},
                     {'line_number': 81, 'words_to_fix': {'generate'}},
                     {'line_number': 86, 'words_to_fix': {'generate'}},
                     {'line_number': 96, 'words_to_fix': {'generate'}},
                     {'line_number': 98, 'words_to_fix': {'generate'}},
                     {'line_number': 100, 'words_to_fix': {'generate'}},
                     {'line_number': 106, 'words_to_fix': {'generate'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = generate.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '011')

        dExpected = [24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_uppercase(self):
        oRule = generate.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [{'line_number': 14, 'words_to_fix': {'generate_1'}},
                     {'line_number': 19, 'words_to_fix': {'generate_1'}},
                     {'line_number': 73, 'words_to_fix': {'generate_3'}},
                     {'line_number': 96, 'words_to_fix': {'generate_3'}},
                     {'line_number': 98, 'words_to_fix': {'generate_2'}},
                     {'line_number': 100, 'words_to_fix': {'generate_1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_lowercase(self):
        oRule = generate.rule_012()
        oRule.case = 'lower'

        dExpected = [{'line_number': 9, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 29, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 34, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 39, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 44, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 49, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 54, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 58, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 62, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 75, 'words_to_fix': {'GENERATE_2'}},
                     {'line_number': 79, 'words_to_fix': {'GENERATE_4'}},
                     {'line_number': 81, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 86, 'words_to_fix': {'GENERATE_1'}},
                     {'line_number': 106, 'words_to_fix': {'GENERATE_1'}}]
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

        dExpected = [21,26]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = generate.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [104]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
