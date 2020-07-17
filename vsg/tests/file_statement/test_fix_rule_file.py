import os

import unittest

from vsg.rules import file_statement
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'file_test_input.vhd'))


class testFixRuleFileMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = file_statement.rule_001()
        lExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
        self.assertEqual(self.oFile.lines[9].line, '  FILE     defaultImage : load_file_type open read_mode is load_file_name;')
        self.assertEqual(self.oFile.lines[11].line, '  file defaultImage : load_file_type open read_mode')
        self.assertEqual(self.oFile.lines[12].line, '    is load_file_name;')

    def test_fix_rule_002(self):
        oRule = file_statement.rule_002()
        lExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
        self.assertEqual(self.oFile.lines[9].line, '   file     defaultImage : load_file_type open read_mode is load_file_name;')
