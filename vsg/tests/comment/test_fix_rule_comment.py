import os
import unittest
import sys

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

#    def test_rule_002(self):
#        oRule = comment.rule_002()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_002_case(self):
#        oRule = comment.rule_002()
#        dExpected = []
#        oRule.fix(oFileCase)
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)

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
