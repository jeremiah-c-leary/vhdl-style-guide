
import unittest

from vsg.rules import variable


class test_rule(unittest.TestCase):

    def test_rule_003(self):
        oRule = variable.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '003')
        self.assertTrue(oRule.deprecated)
