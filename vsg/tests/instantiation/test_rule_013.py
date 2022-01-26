
import unittest

from vsg.rules import instantiation


class test_rule(unittest.TestCase):

    def test_rule_013(self):
        oRule = instantiation.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '013')
        self.assertTrue(oRule.deprecated)
