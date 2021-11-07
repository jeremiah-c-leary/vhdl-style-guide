
import unittest

from vsg.rules import subtype


class test_rule(unittest.TestCase):

    def test_rule_003(self):
        oRule = subtype.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '003')
        self.assertTrue(oRule.deprecated)
