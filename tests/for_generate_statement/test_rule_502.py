# -*- coding: utf-8 -*-

import unittest

from vsg.rules import for_generate_statement


class test_rule(unittest.TestCase):
    def test_rule_502(self):
        oRule = for_generate_statement.rule_502()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "for_generate_statement")
        self.assertEqual(oRule.identifier, "502")
        self.assertTrue(oRule.deprecated)
