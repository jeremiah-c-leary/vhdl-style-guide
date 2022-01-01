
import unittest

from vsg.rules import signal


class test_rule(unittest.TestCase):

    def test_rule_003(self):
        oRule = signal.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '003')
        self.assertTrue(oRule.deprecated)
