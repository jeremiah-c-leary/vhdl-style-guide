# -*- coding: utf-8 -*-

import unittest

from vsg.rules import case


class test_rule(unittest.TestCase):
    def test_rule_500(self):
        oRule = case.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "case")
        self.assertEqual(oRule.identifier, "500")
        self.assertTrue(oRule.deprecated)
