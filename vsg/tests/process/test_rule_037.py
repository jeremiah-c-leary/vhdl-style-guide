import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'rule_037_test_input.vhd'))

class testRuleArchitecture(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule(self):
        oRule = process.rule_037()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '037')

        lExpected = []

        dViolation = utils.add_violation(9)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(11)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(12)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(13)
        dViolation['columnAdjust'] = 1
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['columnAdjust'] = -1
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(32)
        dViolation['columnAdjust'] = -3
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['columnAdjust'] = 1
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(35)
        dViolation['columnAdjust'] = -1
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(62)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 11
        lExpected.append(dViolation)


        dViolation = utils.add_violation(82)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(85)
        dViolation['columnAdjust'] = 4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)


        dViolation = utils.add_violation(100)
        dViolation['columnAdjust'] = -4
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)

        dViolation = utils.add_violation(101)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 13
        lExpected.append(dViolation)


        dViolation = utils.add_violation(115)
        dViolation['columnAdjust'] = 2
        dViolation['targetColumn'] = 12
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

        self.assertEqual('Move identifier to column 14', oRule._get_solution(9))
        self.assertEqual('Move identifier to column 14', oRule._get_solution(11))
        self.assertEqual('Move identifier to column 14', oRule._get_solution(12))
        self.assertEqual('Move identifier to column 14', oRule._get_solution(13))
        self.assertEqual('Move identifier to column 14', oRule._get_solution(30))

#    def test_fix_rule(self):
#        oRule = process.rule_037()
#        dExpected = []
#        oRule.fix(self.oFile)
#
#        self.assertEqual(self.oFile.lines[5].line,  '  variable v_var1 : std_logic;')
#        self.assertEqual(self.oFile.lines[6].line,  '  signal   s_sig1 : std_logic;')
#        self.assertEqual(self.oFile.lines[7].line,  '  constant c_cons1 : std_logic;')
#        self.assertEqual(self.oFile.lines[8].line,  '  file     f_fil1 : load_file_type open read_mode is load_file_name;')
#        self.assertEqual(self.oFile.lines[9].line,  '  type     t_typ1 is (idle, write, read);')
#        self.assertEqual(self.oFile.lines[10].line, '  subtype  s_sub1 is range 0 to 9;')
#
#        self.assertEqual(self.oFile.lines[21].line,  '  variable v_var1 : std_logic;')
#        self.assertEqual(self.oFile.lines[22].line,  '  signal   s_sig1 : std_logic;')
#        self.assertEqual(self.oFile.lines[23].line,  '  constant c_cons1 : std_logic;')
#        self.assertEqual(self.oFile.lines[24].line,  '  file     f_fil1 : load_file_type open read_mode is load_file_name;')
#        self.assertEqual(self.oFile.lines[25].line,  '  type     t_typ1 is (idle, write, read);')
#        self.assertEqual(self.oFile.lines[26].line,  '  subtype  s_sub1 is range 0 to 9;')
#
#        self.assertEqual(self.oFile.lines[44].line,  '  type   state_type is (')
#        self.assertEqual(self.oFile.lines[45].line,  '    state1, state2,')
#        self.assertEqual(self.oFile.lines[46].line,  '    state3, state4')
#        self.assertEqual(self.oFile.lines[48].line,  '  signal sig1 : std_logic;')
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, dExpected)
