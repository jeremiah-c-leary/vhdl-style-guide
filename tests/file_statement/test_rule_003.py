
import unittest

from vsg.rules import file_statement


class test_rule(unittest.TestCase):

    def test_rule_003(self):
        oRule = file_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '003')
        self.assertTrue(oRule.deprecated)
