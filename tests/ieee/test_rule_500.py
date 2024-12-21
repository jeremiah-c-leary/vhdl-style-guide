# -*- coding: utf-8 -*-

import unittest

from vsg.rules import ieee


class test_rule(unittest.TestCase):
    def test_rule_500(self):
        oRule = ieee.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "ieee")
        self.assertEqual(oRule.identifier, "500")
        self.assertTrue(oRule.deprecated)
