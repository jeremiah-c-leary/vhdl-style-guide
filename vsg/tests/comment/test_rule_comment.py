import os
import unittest

from vsg.rules import comment
from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','comment','comment_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileProcess = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','comment','comment_process_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(lFileProcess)
lFileLibrary = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_library_test_input.vhd'))
oFileLibrary = vhdlFile.vhdlFile(lFileLibrary)

class testRuleCommentMethods(unittest.TestCase):

    def test_rule_010(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '010')
        dExpected = utils.add_violation_list([3,7,12,13,17,19,21,23,27,30,45,49,71,75])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_library(self):
        oRuleList = rule_list.rule_list(oFileLibrary)
        oRuleList.check_rules()
        iExpectedFailures = 1
        iFailures = 0
        for oRule in oRuleList.rules:
            iFailures += len(oRule.violations)
        self.assertEqual(iFailures, iExpectedFailures)

    def test_rule_004(self):
        oRule = comment.rule_004()
        dExpected = utils.add_violation_list([39, 58, 61, 62])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
