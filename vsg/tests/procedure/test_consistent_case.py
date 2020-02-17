import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import procedure
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentCase(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_007(self):
        oRule = procedure.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [{'lineNumber': 14, 'procedure': 'Average_samples'}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(14), 'Inconsistent capitalization of word: Average_samples')

    def test_fix_rule_007(self):
        oRule = procedure.rule_007()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[14].line, '    AVERAGE_SAMPLES();')

        self.assertEqual(oRule.violations, [])
