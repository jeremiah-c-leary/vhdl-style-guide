# -*- coding: utf-8 -*-

import unittest

from vsg.rules import case


class test_rule(unittest.TestCase):
    def test_rule_003(self):
        oRule = case.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "case")
        self.assertEqual(oRule.identifier, "013")
        self.assertTrue(oRule.deprecated)
