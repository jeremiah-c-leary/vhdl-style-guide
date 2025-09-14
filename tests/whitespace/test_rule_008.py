# -*- coding: utf-8 -*-

import unittest

from vsg.rules import whitespace


class test_rule(unittest.TestCase):
    def test_rule_008(self):
        oRule = whitespace.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "whitespace")
        self.assertEqual(oRule.identifier, "008")
        self.assertTrue(oRule.deprecated)
