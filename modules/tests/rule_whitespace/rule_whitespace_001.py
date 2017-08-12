
import sys
sys.path.append('..\..')
import unittest
import rule_whitespace
import os


class testRuleWhitespaceMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = rule_whitespace.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = rule_whitespace.rule_001()

        dExpected = [2,4]
        lLines = []
        lLines.append('  This is a test of ending whitespace')
        lLines.append('  This is a test of ending whitespace ')
        lLines.append('  This is a test of ending whitespace')
        lLines.append('  This is a test of ending whitespace  ')
        lLines.append('  This is a test of ending whitespace')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = rule_whitespace.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = rule_whitespace.rule_002()

        dExpected = [1,2,5]
        lLines = []
        lLines.append('  This is a test of tabs\t')
        lLines.append('\tThis is a test of tabs')
        lLines.append('  This is a test of tabs')
        lLines.append('  This is a test of tabs')
        lLines.append('  This is a \t test of tabs')
        lLines.append('  This is a test of tabs')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = rule_whitespace.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = rule_whitespace.rule_003()

        dExpected = [2,4,6]
        lLines = []
        lLines.append('  This is a test of tabs;')
        lLines.append('  This is a test of tabs ;')
        lLines.append('  This is a test of tabs;')
        lLines.append('  This is a test of tabs    ;')
        lLines.append('  This is a test; of tabs')
        lLines.append('  This is a test ; of tabs')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = rule_whitespace.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004(self):
        oRule = rule_whitespace.rule_004()

        dExpected = [2,4,6]
        lLines = []
        lLines.append('  This is a test of tabs,')
        lLines.append('  This is a test of tabs ,')
        lLines.append('  This is a test of tabs,')
        lLines.append('  This is a test of tabs    ,')
        lLines.append('  This is a test, of tabs')
        lLines.append('  This is a test , of tabs')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
