import os

import unittest
import sys

from vsg.rules import function
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','function','function_test_input.vhd'))

class testRuleFunctionMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = function.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [16,17,18,19,21,22,23,24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = function.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [16]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = function.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [28]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = function.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [31]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = function.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [36]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_rule_006(self):
#        oRule = function.rule_006()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '006')
#        dExpected = [9,15,22,30]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_007(self):
#        oRule = function.rule_007()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '007')
#        dExpected = [15,30]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_008(self):
#        oRule = function.rule_008()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '008')
#        dExpected = [15,36]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_009(self):
#        oRule = function.rule_009()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '009')
#        dExpected = [22,42]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_010(self):
#        oRule = function.rule_010()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '010')
#        dExpected = [6]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_011(self):
#        oRule = function.rule_011()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '011')
#        dExpected = [42]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_012(self):
#        oRule = function.rule_012()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '012')
#        dExpected = [51,57]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_013(self):
#        oRule = function.rule_013()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '013')
#        dExpected = [6,27,33]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_014(self):
#        oRule = function.rule_014()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '014')
#        dExpected = [19,33,39]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_015(self):
#        oRule = function.rule_015()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '015')
#        dExpected = [63]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_016(self):
#        oRule = function.rule_016()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '016')
#        dExpected = [6,11,17,24,32,38,51,55]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_017(self):
#        oRule = function.rule_017()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '017')
#        dExpected = [46]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_018(self):
#        oRule = function.rule_018()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '018')
#        dExpected = [9,15,22,30,36,42,53,60]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_019(self):
#        oRule = function.rule_019()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '019')
#        dExpected = [48]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_020(self):
#        oRule = function.rule_020()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '020')
#        dExpected = [19,25,26,27,33]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_021(self):
#        oRule = function.rule_021()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '021')
#        dExpected = [59,70]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_022(self):
#        oRule = function.rule_022()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '022')
#        dExpected = [47,52,59,64]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_023(self):
#        oRule = function.rule_023()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '023')
#        dExpected = [48,53,60,65]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_024(self):
#        oRule = function.rule_024()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '024')
#        dExpected = [63]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_025(self):
#        oRule = function.rule_025()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '025')
#        dExpected = [68]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_026(self):
#        oRule = function.rule_026()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '026')
#        dExpected = [75]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_027(self):
#        oRule = function.rule_027()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '027')
#        dExpected = [77,84]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
