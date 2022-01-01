
import unittest

from vsg.rules import instantiation


class test_rule(unittest.TestCase):

    def test_rule_022(self):
        oRule = instantiation.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '022')
        self.assertTrue(oRule.deprecated)
