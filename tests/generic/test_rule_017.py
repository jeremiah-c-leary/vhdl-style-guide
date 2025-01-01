# -*- coding: utf-8 -*-

import unittest

from vsg.rules import generic


class test_rule(unittest.TestCase):
    def test_rule_017(self):
        oRule = generic.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generic")
        self.assertEqual(oRule.identifier, "017")
        self.assertTrue(oRule.deprecated)
