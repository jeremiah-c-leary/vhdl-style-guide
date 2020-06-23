import os

import unittest

from vsg.rules import function
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','function','function_test_input.vhd'))
lFileMultiple = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'function_multiple_parameters_test_input.vhd'))

class testFixRuleFunctionMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oFileMultiple = vhdlFile.vhdlFile(lFileMultiple)

    def test_fix_rule_001(self):
        oRule = function.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = function.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = function.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = function.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005_lowercase(self):
        oRule = function.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[36].line, '  function func_1 (a : integer) return integer is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005_uppercase(self):
        oRule = function.rule_005()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[4].line, '  FUNCTION func_1 (a : integer) return integer is')
        self.assertEqual(self.oFile.lines[47].line, '  impure FUNCTION func_1 (a : integer) return integer is')
        self.assertEqual(self.oFile.lines[54].line, '  pure FUNCTION func_1 (a : integer) return integer is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = function.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = function.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = function.rule_008()
        self.assertTrue(oRule)
        dExpected = []
        oRule.fix(self.oFileMultiple)
        oRule.analyze(self.oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFileMultiple.lines[5].line, '    c : unsigned(3 downto 0);')
        self.assertFalse(self.oFileMultiple.lines[6].isSignal)
        self.assertEqual(self.oFileMultiple.lines[6].line, '    signal d : std_logic_vector(7 downto 0);')
        self.assertFalse(self.oFileMultiple.lines[7].isConstant)
        self.assertEqual(self.oFileMultiple.lines[7].line, '    constant e : std_logic) return integer is')

    def test_fix_rule_009(self):
        oRule = function.rule_009()
        self.assertTrue(oRule)
        dExpected = []
        oRule.fix(self.oFileMultiple)
        oRule.analyze(self.oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFileMultiple.lines[4].line, '  function func_1 (')
        self.assertEqual(self.oFileMultiple.lines[5].line, '  a : integer; b : integer;')
        self.assertEqual(self.oFileMultiple.lines[6].line, '             c : unsigned(3 downto 0);')

    def test_fix_rule_013(self):
        oRule = function.rule_013()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014(self):
        oRule = function.rule_014()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
