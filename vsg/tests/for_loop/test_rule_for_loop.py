import os

import unittest

from vsg.rules import for_loop
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','for_loop','for_loop_test_input.vhd'))

class testRuleForLoopMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = for_loop.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [19,21,23]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_rule_002(self):
#        oRule = for_loop.rule_002()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '002')
#        dExpected = [8,13,24,33,41,46,52]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_003(self):
#        oRule = for_loop.rule_003()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '003')
#        dExpected = [57]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_004(self):
#        oRule = for_loop.rule_004()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '004')
#        dExpected = [32,57,73]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_005(self):
#        oRule = for_loop.rule_005()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '005')
#        dExpected = [73]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_006(self):
#        oRule = for_loop.rule_006()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '006')
#        dExpected = [68,73,80]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_006_case(self):
#        oRule = for_loop.rule_006()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '006')
#        dExpected = []
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_007(self):
#        oRule = for_loop.rule_007()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '007')
#        dExpected = [73]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_008(self):
#        oRule = for_loop.rule_008()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '008')
#        dExpected = [78,89]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_008_case(self):
#        oRule = for_loop.rule_008()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '008')
#        dExpected = []
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_009(self):
#        oRule = for_loop.rule_009()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '009')
#        dExpected = [20,21,67,68]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_010(self):
#        oRule = for_loop.rule_010()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '010')
#        dExpected = [85]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_010_case(self):
#        oRule = for_loop.rule_010()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '010')
#        dExpected = []
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_011(self):
#        oRule = for_loop.rule_011()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '011')
#        dExpected = [85]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_011_case(self):
#        oRule = for_loop.rule_011()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '011')
#        dExpected = []
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_012(self):
#        oRule = for_loop.rule_012()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '012')
#        dExpected = [98,99,102,105,109]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_013(self):
#        oRule = for_loop.rule_013()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '013')
#        dExpected = [105,109]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_014(self):
#        oRule = for_loop.rule_014()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'for_loop')
#        self.assertEqual(oRule.identifier, '014')
#        dExpected = [105,110]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
