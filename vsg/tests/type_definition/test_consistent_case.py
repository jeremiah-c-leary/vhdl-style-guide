import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import type_definition
from vsg import vhdlFile
from vsg.tests import utils


class testGeneralRule(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_014(self):
        oRule = type_definition.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '014')
        lExpected = []
        dViolation = utils.add_violation(7)
        dViolation['type'] = 'STATE_MACHINE'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(9)
        dViolation['type'] = 'State_Machine'
        lExpected.append(dViolation)
        
#        dExpected = [{'lineNumber': 7, 'type': 'STATE_MACHINE'},
#                     {'lineNumber': 9, 'type': 'State_Machine'}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
        self.assertEqual(oRule._get_solution(7), 'Inconsistent capitalization of word: STATE_MACHINE')
        self.assertEqual(oRule._get_solution(9), 'Inconsistent capitalization of word: State_Machine')

    def test_fix_rule_014(self):
        oRule = type_definition.rule_014()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[7].line, '  signal sm1 : state_machine;')
        self.assertEqual(self.oFile.lines[9].line, '  constant some_const : state_machine;')
        self.assertEqual(self.oFile.lines[13].line, '      SIG1 : in    STATE_MACHINE;')

        self.assertEqual(oRule.violations, [])
