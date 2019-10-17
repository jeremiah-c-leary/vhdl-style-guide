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
        dExpected = [8, 13]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(8), 'Inconsistent capitalization of word: Func_1')
        self.assertEqual(oRule._get_solution(13), 'Inconsistent capitalization of word: FUNC_1')

    def test_fix_rule_010(self):
        oRule = function.rule_010()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[8].line, '  OUT1 <= func_1;')
        self.assertEqual(self.oFile.lines[13].line, '     sig1 <= func_1;')

        self.assertEqual(oRule.violations, [])
