import os
import unittest
import sys

from vsg.rules import comment
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','comment','comment_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','comment','comment_case_test_input.vhd'))
#oFileProcess = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','comment','comment_process_test_input.vhd'))

class testFixRuleCommentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = comment.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

#    def test_rule_001_case(self):
#        oRule = comment.rule_001()
#        oRule.fix(oFileCase)
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, [])

#    def test_rule_002(self):
#        oRule = comment.rule_002()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'comment')
#        self.assertEqual(oRule.identifier, '002')
#        dExpected = [18,19,26,27,30,40,43,44,45,46,49,50,51,52,54,59,62,63,64,65,68,69,70,71,73]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_002_case(self):
#        oRule = comment.rule_002()
#        dExpected = [23]
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_003(self):
#        oRule = comment.rule_003()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'comment')
#        self.assertEqual(oRule.identifier, '003')
#        dExpected = ['26-33','39-46']
#        oRule.analyze(oFileProcess)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_004(self):
#        oRule = comment.rule_004()
#        dExpected = [39]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)

if __name__ == '__main__':
    unittest.main()
