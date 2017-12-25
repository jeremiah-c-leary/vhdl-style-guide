import os

import unittest

from vsg.rules import file_statement
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'file_test_input.vhd'))


class testFixRuleFileMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = file_statement.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[9].line, '  FILE     defaultImage : load_file_type open read_mode is load_file_name;')
        self.assertEqual(oFile.lines[11].line, '  file defaultImage : load_file_type open read_mode')
        self.assertEqual(oFile.lines[12].line, '    is load_file_name;')

    def test_fix_rule_002(self):
        oRule = file_statement.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[9].line, '  file     defaultImage : load_file_type open read_mode is load_file_name;')

    def test_fix_rule_003(self):
        oRule = file_statement.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[9].line, '  file defaultImage : load_file_type open read_mode is load_file_name;')

