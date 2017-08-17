
import sys
sys.path.append('..\..')
import unittest
import rule_library
import os


# Read in test file used for all tests
lLines = []
with open('library_test_input.vhd') as oFile:
    for sLine in oFile:
        lLines.append(sLine.rstrip())
oFile.close()


class testRuleLibraryMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = rule_library.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = rule_library.rule_001()

        dExpected = [7,9,21]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = rule_library.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = rule_library.rule_002()

        dExpected = [13,20,21]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = rule_library.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = rule_library.rule_003()

        dExpected = [21]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = rule_library.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004(self):
        oRule = rule_library.rule_004()

        dExpected = [9,20]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = rule_library.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '005')

    def test_rule_005(self):
        oRule = rule_library.rule_005()

        dExpected = [26,27,29]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = rule_library.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = rule_library.rule_006()

        dExpected = [27,29]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_exists(self):
        oRule = rule_library.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '007')

    def test_rule_007(self):
        oRule = rule_library.rule_007()

        dExpected = [16,23,26,29]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008_exists(self):
        oRule = rule_library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '008')

    def test_rule_008(self):
        oRule = rule_library.rule_008()

        dExpected = [14,16,26,29]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

if __name__ == '__main__':
    unittest.main()
