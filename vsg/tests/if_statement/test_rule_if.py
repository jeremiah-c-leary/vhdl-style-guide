import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))


class testRuleIfMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = if_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [13,33]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = if_statement.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [8,13,24,33,41,46,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = if_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [57]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = if_statement.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [32,57,73]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = if_statement.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [73]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = if_statement.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [68,73,80]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_case(self):
        oRule = if_statement.rule_006()
        dExpected = [9,20]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = if_statement.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [73]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_case(self):
        oRule = if_statement.rule_007()
        dExpected = [20]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = if_statement.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [78,89]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008_case(self):
        oRule = if_statement.rule_008()
        dExpected = [42]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = if_statement.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [20,21,67,68,115]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = if_statement.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [85]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_case(self):
        oRule = if_statement.rule_010()
        dExpected = [31]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = if_statement.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [85]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_case(self):
        oRule = if_statement.rule_011()
        dExpected = [31]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = if_statement.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [24,108]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = if_statement.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [85,109]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = if_statement.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '014')
        dExpected = [11,27,36,39,60,110]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = if_statement.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [117]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = if_statement.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '020')
        dExpected = [105,110]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = if_statement.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '021')
        dExpected = [105,109]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = if_statement.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '022')
        dExpected = [102,105]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = if_statement.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '023')
        dExpected = [108]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = if_statement.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '024')
        dExpected = [98,99,105,109]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025(self):
        oRule = if_statement.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '025')
        dExpected = [13]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_026(self):
        oRule = if_statement.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '026')
        dExpected = [24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_027(self):
        oRule = if_statement.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '027')
        dExpected = [94]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_028(self):
        oRule = if_statement.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '028')
        dExpected = [17,27]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_029(self):
        oRule = if_statement.rule_029()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '029')
        dExpected = [14]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
