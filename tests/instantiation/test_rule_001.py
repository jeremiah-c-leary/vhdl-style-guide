# -*- coding: utf-8 -*-

import unittest

from vsg.rules import instantiation


class test_rule(unittest.TestCase):
    def test_rule_001(self):
        oRule = instantiation.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "instantiation")
        self.assertEqual(oRule.identifier, "001")
        self.assertTrue(oRule.deprecated)
