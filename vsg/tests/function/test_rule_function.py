import os

import unittest

from vsg.rules import function
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'function_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileMultiple = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'function_multiple_parameters_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(lFileMultiple)


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

    def test_rule_005_lowercase(self):
        oRule = function.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [36]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_uppercase(self):
        oRule = function.rule_005()
        oRule.case = 'upper'
        dExpected = [4,16,21,28,47,54,63,70,78,87,97,110,126,128,136,141,146]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = function.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = function.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [19,24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = function.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [5,6,7]
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = function.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [4]
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)
