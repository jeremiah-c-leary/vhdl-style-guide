import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import variable
from vsg import vhdlFile


class testFixRuleVariableMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))

    def test_fix_rule_001(self):
        oRule = variable.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = variable.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = variable.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = variable.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = variable.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = variable.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = variable.rule_007()
        self.assertFalse(oRule.fixable)

    def test_fix_rule_009(self):
        oRule = variable.rule_009()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = variable.rule_010()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = variable.rule_011()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[27].line, '    variable p1_variable_1       : std_logic;')
        self.assertEqual(self.oFile.lines[28].line, '    variable p1_variable_10      : integer;')
        self.assertEqual(self.oFile.lines[29].line, '    variable p1_variable_long_10 : real;')
        self.assertEqual(self.oFile.lines[37].line, '    variable p1_var_1       : std_logic;')
        self.assertEqual(self.oFile.lines[38].line, '    variable p1_var_10      : integer;')
        self.assertEqual(self.oFile.lines[39].line, '    variable p1_var_long_10 : real;')
        self.assertEqual(self.oFile.lines[47].line, '    variable process1_variable_1       : std_logic;')
        self.assertEqual(self.oFile.lines[48].line, '    variable process1_variable_10      : integer;')
        self.assertEqual(self.oFile.lines[49].line, '    variable process1_variable_long_10 : real;')

