# -*- coding: utf-8 -*-

import unittest

from vsg.rules import iteration_scheme


class test_rule(unittest.TestCase):
    def test_rule_502(self):
        oRule = iteration_scheme.rule_502()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "iteration_scheme")
        self.assertEqual(oRule.identifier, "502")
        self.assertTrue(oRule.deprecated)
