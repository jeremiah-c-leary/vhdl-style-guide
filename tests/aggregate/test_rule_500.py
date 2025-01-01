# -*- coding: utf-8 -*-

import unittest

from vsg.rules import aggregate


class test_rule(unittest.TestCase):
    def test_rule_500(self):
        oRule = aggregate.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "aggregate")
        self.assertEqual(oRule.identifier, "500")
        self.assertTrue(oRule.deprecated)
