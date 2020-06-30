import os
import unittest

from vsg.rules import function
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'rule_015_016_test_input.vhd'))

class testRuleArchitecture(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

#    def test_rule_015(self):
#        oRule = function.rule_015()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'function')
#        self.assertEqual(oRule.identifier, '015')
#
#        lExpected = []
#
#        dViolation = utils.add_violation(9)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(10)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(11)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(42)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 16
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(43)
#        dViolation['columnAdjust'] = 2 
#        dViolation['targetColumn'] = 16
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(44)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 16
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(66)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(67)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(68)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(86)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 13
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(113)
#        dViolation['columnAdjust'] = -1
#        dViolation['targetColumn'] = 14
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(114)
#        dViolation['columnAdjust'] = 2
#        dViolation['targetColumn'] = 14
#        lExpected.append(dViolation)
#
#        dViolation = utils.add_violation(115)
#        dViolation['columnAdjust'] = 1
#        dViolation['targetColumn'] = 14
#        lExpected.append(dViolation)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, lExpected)
#
#        self.assertEqual('Move identifier to column 14', oRule._get_solution(9))
#        self.assertEqual('Move identifier to column 14', oRule._get_solution(11))
#
#    def test_fix_rule_015(self):
#        oRule = function.rule_015()
#        oRule.fix(self.oFile)
#
##        self.assertEqual(self.oFile.lines[5].line,  '  variable v_var1 : std_logic;')
#        self.assertEqual(self.oFile.lines[8].line,  '    constant a : integer;')
#        self.assertEqual(self.oFile.lines[9].line,  '    signal   b : integer;')
#        self.assertEqual(self.oFile.lines[10].line, '    signal   c : unsigned(3 downto 0);')
#        self.assertEqual(self.oFile.lines[11].line, '    signal   d : std_logic_vector(7 downto 0);')
#        self.assertEqual(self.oFile.lines[12].line, '    constant e : std_logic) return integer is')
#        self.assertEqual(self.oFile.lines[13].line, '    file file1 : load_file_type open read_mode is load_file_name;')
#        self.assertEqual(self.oFile.lines[14].line, '    constant con1 : integer := 0;')
#        self.assertEqual(self.oFile.lines[15].line, '    signal sig1 : std_logic_vector;')
#
#        dExpected = []
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = function.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '015')

        lExpected = []

        dViolation = utils.add_violation(13)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(15)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(46)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 16
        lExpected.append(dViolation)

        dViolation = utils.add_violation(48)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 16
        lExpected.append(dViolation)

        dViolation = utils.add_violation(117)
        dViolation['columnAdjust'] = 4 
        dViolation['targetColumn'] = 14
        lExpected.append(dViolation)

        dViolation = utils.add_violation(119)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 14
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

        self.assertEqual('Move identifier to column 14', oRule._get_solution(13))
        self.assertEqual('Move identifier to column 14', oRule._get_solution(15))

    def test_fix_rule_015(self):
        oRule = function.rule_015()
        oRule.fix(self.oFile)

        self.assertEqual(self.oFile.lines[8].line,  '    constant a : integer;')
        self.assertEqual(self.oFile.lines[9].line,  '    signal b : integer;')
        self.assertEqual(self.oFile.lines[10].line, '    signal c : unsigned(3 downto 0);')
        self.assertEqual(self.oFile.lines[11].line, '    signal d : std_logic_vector(7 downto 0);')
        self.assertEqual(self.oFile.lines[12].line, '    constant e : std_logic) return integer is')
        self.assertEqual(self.oFile.lines[13].line, '    file     file1 : load_file_type open read_mode is load_file_name;')
        self.assertEqual(self.oFile.lines[14].line, '    constant con1 : integer := 0;')
        self.assertEqual(self.oFile.lines[15].line, '    signal   sig1 : std_logic_vector;')

        dExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
