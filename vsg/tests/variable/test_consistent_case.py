import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentCase(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_011(self):
        oRule = variable.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '011')
        lExpected = []
        dViolation = utils.add_violation(16)
        dViolation['variable'] = 'Var1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(18)
        dViolation['variable'] = 'VAR2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(19)
        dViolation['variable'] = 'vaR3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['variable'] = 'VAR4'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['variable'] = 'vaR1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['variable'] = 'VAR2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['variable'] = 'Var3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['variable'] = 'vAr4'
        lExpected.append(dViolation)
#
#
#        dExpected = [{'lineNumber': 16, 'variable': 'Var1'},
#                     {'lineNumber': 18, 'variable': 'VAR2'},
#                     {'lineNumber': 19, 'variable': 'vaR3'},
#                     {'lineNumber': 21, 'variable': 'VAR4'},
#                     {'lineNumber': 24, 'variable': 'vaR1'},
#                     {'lineNumber': 24, 'variable': 'VAR2'},
#                     {'lineNumber': 24, 'variable': 'Var3'},
#                     {'lineNumber': 24, 'variable': 'vAr4'}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
        self.assertEqual(oRule._get_solution(16), 'Inconsistent capitalization of word: Var1')
        self.assertEqual(oRule._get_solution(18), 'Inconsistent capitalization of word: VAR2')
        self.assertEqual(oRule._get_solution(19), 'Inconsistent capitalization of word: vaR3')
        self.assertEqual(oRule._get_solution(21), 'Inconsistent capitalization of word: VAR4')
        self.assertEqual(oRule._get_solution(24), 'Inconsistent capitalization of words: vaR1, VAR2, Var3, vAr4')

    def test_fix_rule_011(self):
        oRule = variable.rule_011()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[16].line, '    var1 <= \'0\';')
        self.assertEqual(self.oFile.lines[18].line, '    if (var2 = \'0\') then')
        self.assertEqual(self.oFile.lines[19].line, '      var3 <= \'1\';')
        self.assertEqual(self.oFile.lines[21].line, '      var4 <= \'0\';')

        self.assertEqual(oRule.violations, [])
