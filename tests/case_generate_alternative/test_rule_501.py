# -*- coding: utf-8 -*-

import unittest

from vsg.rules import case_generate_alternative


class test_rule(unittest.TestCase):
    def test_rule_501(self):
        oRule = case_generate_alternative.rule_501()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "case_generate_alternative")
        self.assertEqual(oRule.identifier, "501")
        self.assertTrue(oRule.deprecated)
