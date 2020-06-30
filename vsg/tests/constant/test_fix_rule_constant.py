import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'constant_test_input.vhd'))

class testFixRuleConstantMethods(unittest.TestCase):

    def setUp(self):

        # Process the test file used for all tests
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = constant.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  '  Constant c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  '  constant const  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '  constant c_const: std_logic')

    def test_fix_rule_002(self):
        oRule = constant.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  constant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'constant c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const: std_logic')

        oRule = constant.rule_002()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  CONSTANT c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  CONSTANT const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  CONSTANT  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'CONSTANT c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'CONSTANT const  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   CONSTANT c_const: std_logic')

    def test_fix_rule_004(self):
        oRule = constant.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant c_const :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const: std_logic')

        oRule = constant.rule_004()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant C_CONST : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant CONST : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  C_CONST : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant C_CONST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant CONST  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant C_CONST: std_logic')

    def test_fix_rule_005(self):
        oRule = constant.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant c_coNST : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  : STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const: std_logic')

    def test_fix_rule_006(self):
        oRule = constant.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const : std_logic')

    def test_fix_rule_007(self):
        oRule = constant.rule_007()
        self.assertFalse(oRule.fixable)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  :  STD_LOGIC:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const: std_logic')

    def test_fix_rule_010(self):
        oRule = constant.rule_010()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  :  STD_LOGIC :=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const: std_logic')
        self.assertEqual(self.oFile.lines[38].line, '  constant const : std_logic   := \'0\';')

    def test_fix_rule_011(self):
        oRule = constant.rule_011()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[5].line,  '  constant c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[6].line,  '  constant const : std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[7].line,  '  COnstant  c_const : std_logic := \'1\';')
        self.assertEqual(self.oFile.lines[8].line,  'Constant c_coNST :  std_logic := \'0\';')
        self.assertEqual(self.oFile.lines[9].line,  'constant const  :  std_logic:=\'0\';')
        self.assertEqual(self.oFile.lines[10].line, '   constant c_const: std_logic')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = constant.rule_012()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[31].line, '  (')
        self.assertEqual(self.oFile.lines[32].line, '    0,')
        self.assertEqual(self.oFile.lines[33].line, '    1,')
        self.assertEqual(self.oFile.lines[34].line, '    2,')
        self.assertEqual(self.oFile.lines[35].line, '    3')
        self.assertEqual(self.oFile.lines[36].line, '  );')

    def test_fix_rule_014(self):
        oRule = constant.rule_014()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[40].line, '  constant c_length_constant : integer := I_FOO\'length     + I_BAR\'length +')
        self.assertEqual(self.oFile.lines[41].line, '                                          I_MOREFOO\'length + I_MOREBAR\'length + 1;')
        self.assertEqual(self.oFile.lines[43].line, '  constant c_length_constant : integer := I_FOO\'length     + I_BAR\'length +')
        self.assertEqual(self.oFile.lines[44].line, '                                          I_MOREFOO\'length + I_MOREBAR\'length + 1;')
        self.assertEqual(oRule.violations, dExpected)
