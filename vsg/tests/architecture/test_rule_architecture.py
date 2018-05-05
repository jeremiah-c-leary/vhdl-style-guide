import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_comment_test_input.vhd'))
oFileIs = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'architecture_is_test_input.vhd'))

class testRuleArchitectureMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = architecture.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = architecture.rule_001()

        dExpected = [9,20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = architecture.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = architecture.rule_002()

        dExpected = [14]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = architecture.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = architecture.rule_003()

        dExpected = [14]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = architecture.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004(self):
        oRule = architecture.rule_004()

        dExpected = [20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = architecture.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '005')

    def test_rule_005(self):
        oRule = architecture.rule_005()

        dExpected = [26]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = architecture.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = architecture.rule_006()

        dExpected = [2,9]
        oRule.analyze(oFileIs)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = architecture.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [22]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = architecture.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [24,31]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = architecture.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [7,13,24,31]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = architecture.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [55,71]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = architecture.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = architecture.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [7,18]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = architecture.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [3,20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = architecture.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '014')
        dExpected = [9,20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = architecture.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [26,33]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = architecture.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '016')
        dExpected = [34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = architecture.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '017')
        dExpected = [34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = architecture.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '018')
        dExpected = [35]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = architecture.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '019')
        dExpected = [20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = architecture.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '020')
        dExpected = [20,33]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = architecture.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '021')
        dExpected = [29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = architecture.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '022')
        dExpected = [31]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = architecture.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '023')
        dExpected = ['2-10']
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = architecture.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '024')
        dExpected = [13,71]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
