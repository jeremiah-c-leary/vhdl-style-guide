import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)
lFileCompress = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_compressed_line_test_input.vhd'))
oFileCompress = vhdlFile.vhdlFile(lFileCompress)
lFileNested = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_nested_test_input.vhd'))
oFileNested = vhdlFile.vhdlFile(lFileNested)
lFileIf = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_if_input.vhd'))
oFileIf = vhdlFile.vhdlFile(lFileIf)


oSeverityList = severity.create_list({})

class testFixRuleIfMethods(unittest.TestCase):

    @unittest.skip('This test will eventually be re-written for the new parser.')
    def test_fix_rule_002(self):
        oRule = if_statement.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oFile.lines[13].line, '   if ( a = 1 or d = 20 or    -- this if should not be replaced')
        self.assertEqual(oFile.lines[14].line, '       g = 34 or x = 3000 ) then')
        self.assertEqual(oFile.lines[24].line, '   elsif ( z = 45 and f = 45 ) then')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = if_statement.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = if_statement.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = if_statement.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = if_statement.rule_009()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
