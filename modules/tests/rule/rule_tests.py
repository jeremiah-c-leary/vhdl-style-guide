
import sys
sys.path.append('..\..')
import unittest
import rule
import os


class testRuleMethods(unittest.TestCase):

    def test_rule_exists(self):
        oRule = rule.rule()
        self.assertTrue(oRule)

    def test_rule_name(self):
        oRule = rule.rule()
        self.assertFalse(oRule.name)
        oRule.name = 'sName'
        self.assertEqual(oRule.name, 'sName')

    def test_rule_id(self):
        oRule = rule.rule()
        self.assertFalse(oRule.id)
        oRule.id = 'rule id 001'
        self.assertEqual(oRule.id, 'rule id 001')


if __name__ == '__main__':
    unittest.main()
