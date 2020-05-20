import os
import unittest

from vsg.rules import comment
from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileProcess = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_process_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(lFileProcess)
lFileLibrary = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_library_test_input.vhd'))
oFileLibrary = vhdlFile.vhdlFile(lFileLibrary)


class testFixRuleCommentMethods(unittest.TestCase):

    def test_rule_010(self):
        oRule = comment.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_004(self):
        oRule = comment.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001(self):
        oRuleList = rule_list.rule_list(oFileLibrary)
        oRuleList.fix()
        oRuleList.check_rules()

        self.assertEqual(oFileLibrary.lines[3].indentLevel, 1)
        self.assertEqual(oFileLibrary.lines[7].indentLevel, 1)

        self.assertEqual(oFileLibrary.lines[3].line, '  -- Comment 1')
        self.assertEqual(oFileLibrary.lines[7].line, '  -- Comment 1')

        oRuleList = rule_list.rule_list(oFileLibrary)
        oRuleList.check_rules()
        iExpectedFailures = 0
        iFailures = 0
        for oRule in oRuleList.rules:
            iFailures += len(oRule.violations)
        self.assertEqual(iFailures, iExpectedFailures)
