
import unittest
import sys
sys.path.append('modules')

from modules.rules import rule_comment
from modules import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile('tests/rule_comment/comment_test_input.vhd')

class testRuleCommentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_comment.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [3,7,12,13,21,23]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001_case(self):
        oRule = rule_comment.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [22,26]
        oRule.analyze(vhdlFile.vhdlFile('tests/rule_comment/comment_case_test_input.vhd'))
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_comment.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [18,19,26,27,30,40,43,44,45,46,49,50,51,52,54,59,62,63,64,65,68,69,70,71,73]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_case(self):
        oRule = rule_comment.rule_002()
        dExpected = [23]
        oRule.analyze(vhdlFile.vhdlFile('tests/rule_comment/comment_case_test_input.vhd'))
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_comment.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '003')
        dExpected = ['26-33','39-46']
        oRule.analyze(vhdlFile.vhdlFile('tests/rule_comment/comment_process_test_input.vhd'))
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
