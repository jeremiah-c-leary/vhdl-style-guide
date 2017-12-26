import os

import unittest

from vsg.rules import function
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','function','function_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'function_multiple_parameters_test_input.vhd'))


class testFixRuleFunctionMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = function.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = function.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = function.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = function.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = function.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = function.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = function.rule_007()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = function.rule_008()
        self.assertTrue(oRule)
        dExpected = []
        oRule.fix(oFileMultiple)
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileMultiple.lines[5].line, '    c : unsigned(3 downto 0);')
        self.assertFalse(oFileMultiple.lines[6].isSignal)
        self.assertEqual(oFileMultiple.lines[6].line, '    signal d : std_logic_vector(7 downto 0);')
        self.assertFalse(oFileMultiple.lines[7].isConstant)
        self.assertEqual(oFileMultiple.lines[7].line, '    constant e : std_logic) return integer is')

    def test_fix_rule_009(self):
        oRule = function.rule_009()
        self.assertTrue(oRule)
        dExpected = []
        oRule.fix(oFileMultiple)
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileMultiple.lines[4].line, '  function func_1 (')
        self.assertEqual(oFileMultiple.lines[5].line, '  a : integer; b : integer;')
        self.assertEqual(oFileMultiple.lines[6].line, '    c : unsigned(3 downto 0);')
