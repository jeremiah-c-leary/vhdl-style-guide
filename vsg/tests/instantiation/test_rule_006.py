
import unittest

from vsg.rules import instantiation


class test_rule(unittest.TestCase):

    def test_rule_006(self):
        oRule = instantiation.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '006')
        self.assertTrue(oRule.deprecated)
