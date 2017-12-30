import os

import unittest

from vsg.rules import procedure
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'procedure_test_input.vhd'))


class testFixRuleProcedureMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = procedure.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[14].line, '  procedure AVERAGE_SAMPLES;')
        self.assertEqual(oFile.lines[16].line, '  procedure AVERAGE_SAMPLES (')
        self.assertEqual(oFile.lines[40].line, '  procedure AVERAGE_SAMPLES is')

    def test_fix_rule_005(self):
        oRule = procedure.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[89].line, '    variable var_1 : integer;')
        self.assertEqual(oFile.lines[90].line, '    variable var_2 : integer;')

