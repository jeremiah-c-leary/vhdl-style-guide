# -*- coding: utf-8 -*-

import unittest

from vsg.rules import function


class test_rule(unittest.TestCase):
    def test_rule_014(self):
        oRule = function.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "function")
        self.assertEqual(oRule.identifier, "014")
        self.assertTrue(oRule.deprecated)
