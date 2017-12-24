import os
import unittest

from vsg.rules import comment
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','comment','comment_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','comment','comment_case_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','comment','comment_process_test_input.vhd'))


class testFixRuleCommentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = comment.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003(self):
        oRule = comment.rule_003()
        dExpected = []
        oRule.fix(oFileProcess)
        oRule.analyze(oFileProcess)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = comment.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = comment.rule_005()
        dExpected = []
        oRule.fix(oFileCase)
        oRuleIndex = comment.rule_001()
        oRuleIndex.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileCase.lines[23].indentLevel, 3)
        self.assertEqual(oFileCase.lines[24].indentLevel, 3)
        self.assertEqual(oFileCase.lines[25].indentLevel, 3)

        self.assertEqual(oFileCase.lines[23].line, '      -- Comment 1')
        self.assertEqual(oFileCase.lines[24].line, '      -- Comment 2')
        self.assertEqual(oFileCase.lines[25].line, '      -- Comment 3')

    def test_rule_006(self):
        oRule = comment.rule_006()
        dExpected = []
        oRule.fix(oFileProcess)
        oRule.analyze(oFileProcess)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileProcess.lines[37].line, '      variable a : integer 0 to 10;        -- comment')
        self.assertEqual(oFileProcess.lines[38].line, '      variable b : natural 0 to 256;       -- comment')
