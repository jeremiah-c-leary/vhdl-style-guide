import os
import unittest

from vsg.rules import procedure
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'rule_010_test_input.vhd'))

class testRuleArchitecture(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_015(self):
        oRule = procedure.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '010')

        lExpected = []

        dViolation = utils.add_violation(31)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(32)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)


        dViolation = utils.add_violation(97)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(98)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)


        dViolation = utils.add_violation(123)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 15
        lExpected.append(dViolation)

        dViolation = utils.add_violation(124)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 15
        lExpected.append(dViolation)

        dViolation = utils.add_violation(140)
        dViolation['columnAdjust'] = -2
        dViolation['targetColumn'] = 17
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

        self.assertEqual('Move identifier to column 14', oRule._get_solution(31))
        self.assertEqual('Move identifier to column 14', oRule._get_solution(32))

#    def test_fix_rule_015(self):
#        oRule = function.rule_015()
#        oRule.fix(self.oFile)
#
#        self.assertEqual(self.oFile.lines[8].line,  '    constant a : integer;')
#        self.assertEqual(self.oFile.lines[9].line,  '    signal b : integer;')
#        self.assertEqual(self.oFile.lines[10].line, '    signal c : unsigned(3 downto 0);')
#        self.assertEqual(self.oFile.lines[11].line, '    signal d : std_logic_vector(7 downto 0);')
#        self.assertEqual(self.oFile.lines[12].line, '    constant e : std_logic) return integer is')
#        self.assertEqual(self.oFile.lines[13].line, '    file     file1 : load_file_type open read_mode is load_file_name;')
#        self.assertEqual(self.oFile.lines[14].line, '    constant con1 : integer := 0;')
#        self.assertEqual(self.oFile.lines[15].line, '    signal   sig1 : std_logic_vector;')
#
#        dExpected = []
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, dExpected)
