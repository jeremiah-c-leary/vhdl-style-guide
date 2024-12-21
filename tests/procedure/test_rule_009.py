# -*- coding: utf-8 -*-

import unittest

from vsg.rules import procedure


class test_rule(unittest.TestCase):
    def test_rule_009(self):
        oRule = procedure.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "009")
        self.assertTrue(oRule.deprecated)
