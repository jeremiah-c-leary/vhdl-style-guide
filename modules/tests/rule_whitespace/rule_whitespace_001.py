
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

        dExpected = {'whitespace' : {'001' :[1,3]}}
        lLines = []
        lLines.append('  This is a test of ending whitespace')
        lLines.append('  This is a test of ending whitespace ')
        lLines.append('  This is a test of ending whitespace')
        lLines.append('  This is a test of ending whitespace  ')
        lLines.append('  This is a test of ending whitespace')
        self.assertEqual(oRule.analyze(lLines), dExpected)

    def test_rule_002(self):
        oRule = rule_whitespace.rule_002()

        dExpected = {'whitespace' : {'002' :[0,1,4]}}
        lLines = []
        lLines.append('  This is a test of tabs\t')
        lLines.append('\tThis is a test of tabs')
        lLines.append('  This is a test of tabs')
        lLines.append('  This is a test of tabs')
        lLines.append('  This is a \t test of tabs')
        lLines.append('  This is a test of tabs')
        self.assertEqual(oRule.analyze(lLines), dExpected)


if __name__ == '__main__':
    unittest.main()
