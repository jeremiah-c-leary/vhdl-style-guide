
import unittest

from vsg.rules import type_definition


class test_rule(unittest.TestCase):

    def test_rule_003(self):
        oRule = type_definition.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '003')
        self.assertTrue(oRule.deprecated)
