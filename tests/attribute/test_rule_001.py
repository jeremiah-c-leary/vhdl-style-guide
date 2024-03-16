# -*- coding: utf-8 -*-

import unittest

from vsg.rules import attribute


class test_rule(unittest.TestCase):

    def test_rule_001(self):
        oRule = attribute.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'attribute')
        self.assertEqual(oRule.identifier, '001')
        self.assertTrue(oRule.deprecated)
