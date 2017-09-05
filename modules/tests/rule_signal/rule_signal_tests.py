
import sys
sys.path.append('..\..')
import unittest
import rule_signal
import os


# Read in test file used for all tests
lLines = []
with open('signal_test_input.vhd') as oFile:
    for sLine in oFile:
        lLines.append(sLine.rstrip())
oFile.close()


class testRuleEntityMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = rule_signal.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [6,8,15]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = rule_signal.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [7,11,13]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = rule_signal.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [8,9,12]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = rule_signal.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [6,9,12,15]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = rule_signal.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [6,10,13,14,16,20,21]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = rule_signal.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [7,11,19,21]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_exists(self):
        oRule = rule_signal.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [11,16]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

if __name__ == '__main__':
    unittest.main()
