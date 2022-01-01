
import unittest

from vsg.rules import instantiation


class test_rule(unittest.TestCase):

    def test_rule_021(self):
        oRule = instantiation.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '021')
        self.assertTrue(oRule.deprecated)
