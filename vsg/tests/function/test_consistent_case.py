import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import function
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentCase(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_010(self):
        oRule = function.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '010')

        lExpected = []
        dViolation = utils.add_violation(9)
        dViolation['name'] = 'Func_1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(14)
        dViolation['name'] = 'FUNC_1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(15)
        dViolation['name'] = 'FUNC_1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(15)
        dViolation['name'] = 'funC_2'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
        self.assertEqual(oRule._get_solution(9), 'Inconsistent capitalization of word: Func_1')
        self.assertEqual(oRule._get_solution(14), 'Inconsistent capitalization of word: FUNC_1')
        self.assertEqual(oRule._get_solution(15), 'Inconsistent capitalization of words: FUNC_1, funC_2')

    def test_fix_rule_010(self):
        oRule = function.rule_010()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[9].line, '  OUT1 <= func_1;')
        self.assertEqual(self.oFile.lines[14].line, '     sig1 <= func_1;')
        self.assertEqual(self.oFile.lines[15].line, '     sig2 <= func_1(a) or func_2(b);')

        self.assertEqual(oRule.violations, [])
