import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)
lFileIf = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_if_input.vhd'))
oFileIf = vhdlFile.vhdlFile(lFileIf)

class testRuleIfMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = if_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([13,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = if_statement.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([8,13,24,33,41,46,52])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = if_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [utils.add_violation(57)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = if_statement.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([32,57,73])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = if_statement.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [utils.add_violation(73)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = if_statement.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '006')
        dExpected = utils.add_violation_list([68,73,80])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_case(self):
        oRule = if_statement.rule_006()
        dExpected = utils.add_violation_list([9,20])
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = if_statement.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [utils.add_violation(73)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_case(self):
        oRule = if_statement.rule_007()
        dExpected = [utils.add_violation(20)]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = if_statement.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '008')
        dExpected = utils.add_violation_list([78,89])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008_case(self):
        oRule = if_statement.rule_008()
        dExpected = [utils.add_violation(42)]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = if_statement.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '009')
        dExpected = utils.add_violation_list([20,21,67,68,115])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = if_statement.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [utils.add_violation(85)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_case(self):
        oRule = if_statement.rule_010()
        dExpected = [utils.add_violation(31)]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = if_statement.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [utils.add_violation(85)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_case(self):
        oRule = if_statement.rule_011()
        dExpected = [utils.add_violation(31)]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = if_statement.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([24,108])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = if_statement.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '013')
        dExpected = utils.add_violation_list([85,109])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = if_statement.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '014')
        dExpected = utils.add_violation_list([11,27,36,39,60,110])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = if_statement.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [utils.add_violation(117)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = if_statement.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '020')
        dExpected = utils.add_violation_list([105,110])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = if_statement.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '021')
        dExpected = utils.add_violation_list([105,109])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = if_statement.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '022')
        dExpected = utils.add_violation_list([102,105])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = if_statement.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '023')
        dExpected = [utils.add_violation(108)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = if_statement.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '024')
        dExpected = utils.add_violation_list([98,99,105,109])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025(self):
        oRule = if_statement.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '025')
        dExpected = [{'lines':[{'number': 13}], 'words_to_fix': {'IF'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_026(self):
        oRule = if_statement.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '026')
        dExpected = [{'lines':[{'number': 24}], 'words_to_fix': {'ELSIF'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_027(self):
        oRule = if_statement.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '027')
        dExpected = [{'lines':[{'number': 94}], 'words_to_fix': {'ELSE'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_028(self):
        oRule = if_statement.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '028')
        dExpected = [{'lines':[{'number': 17}], 'words_to_fix': {'END'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_029(self):
        oRule = if_statement.rule_029()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '029')
        dExpected = [{'lines':[{'number': 14}], 'words_to_fix': {'THEN'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_032(self):
        oRule = if_statement.rule_032()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '032')
        lExpected = [{'lines':[{'number': 17}], 'indent': 2},
                     {'lines':[{'number': 16}], 'indent': 2},
                     {'lines':[{'number': 15}], 'indent': 2},
                     {'lines':[{'number': 21}], 'indent': 2},
                     {'lines':[{'number': 20}], 'indent': 2}]
        oRule.analyze(oFileIf)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_033(self):
        oRule = if_statement.rule_033()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '033')
        lExpected = [{'lines':[{'number': 25}], 'indent': 2},
                     {'lines':[{'number': 24}], 'indent': 2}]
        oRule.analyze(oFileIf)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_034(self):
        oRule = if_statement.rule_034()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '034')
        dExpected = [{'lines':[{'number': 27}], 'words_to_fix': {'IF'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
