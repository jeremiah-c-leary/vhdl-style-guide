import os

import unittest

from vsg.rules import for_loop
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'for_loop_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleForLoopMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = for_loop.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [19,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = for_loop.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [23]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = for_loop.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [36, 40]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = for_loop.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [40,48]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = for_loop.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [44,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
