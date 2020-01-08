import os
import unittest

from vsg.rules import comment
from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','comment','comment_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','comment','comment_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)
lFileProcess = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','comment','comment_process_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(lFileProcess)
lFileLibrary = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_library_test_input.vhd'))
oFileLibrary = vhdlFile.vhdlFile(lFileLibrary)
lFileIf = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_if_input.vhd'))
oFileIf = vhdlFile.vhdlFile(lFileIf)

class testRuleCommentMethods(unittest.TestCase):

    def test_rule_010(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [3,7,12,13,17,19,21,23,27,30,45,49,71,75]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_case(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [23,24,25,29]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_library(self):
        oRuleList = rule_list.rule_list(oFileLibrary)
        oRuleList.check_rules()
        iExpectedFailures = 1
        iFailures = 0
        for oRule in oRuleList.rules:
            iFailures += len(oRule.violations)
        self.assertEqual(iFailures, iExpectedFailures)

    def test_rule_003(self):
        oRule = comment.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '003')
        dExpected = ['26-33','39-46']
        oRule.analyze(oFileProcess)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = comment.rule_004()
        dExpected = [39, 58, 61, 62]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = comment.rule_005()
        dExpected = [19,25,24,23]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = comment.rule_006()
        dExpected = ['36-39']
        oRule.analyze(oFileProcess)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001(self):
        oRule = comment.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [4]
        oRule.analyze(oFileLibrary)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = comment.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '008')
        lExpected = [17,16,15,21,20]
        oRule.analyze(oFileIf)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_009(self):
        oRule = comment.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '009')
        lExpected = [25,24]
        oRule.analyze(oFileIf)
        self.assertEqual(oRule.violations, lExpected)
