import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'concurrent_007_test_input.vhd'))

class testRuleConcurrentMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_007_w_default_options(self):
        oRule = concurrent.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [{'lineNumber': 10, 'slice_index': [43]},
                     {'lineNumber': 11, 'slice_index': [43]},
                     {'lineNumber': 16, 'slice_index': [43, 76]},
                     {'lineNumber': 17, 'slice_index': [43, 76]}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_w_allow_single_line_option_enabled(self):
        oRule = concurrent.rule_007()
        oRule.allow_single_line = True
        dExpected = [{'lineNumber': 16, 'slice_index': [43, 76]},
                     {'lineNumber': 17, 'slice_index': [43, 76]}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007_w_default_options(self):
        oRule = concurrent.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[10].line, '  O_FOO <= w_foo when (w_foo_en = \'1\') else')
        self.assertFalse(self.oFile.lines[10].isEndConcurrent)
        self.assertEqual(self.oFile.lines[11].line, ' \'Z\';')
        self.assertTrue(self.oFile.lines[11].insideConcurrent)
        self.assertTrue(self.oFile.lines[11].isEndConcurrent)

        self.assertEqual(self.oFile.lines[12].line, '  O_BAR <= w_bar when (w_bar_en = \'0\') else')
        self.assertFalse(self.oFile.lines[12].isEndConcurrent)
        self.assertEqual(self.oFile.lines[13].line, ' \'1\';')
        self.assertTrue(self.oFile.lines[13].insideConcurrent)
        self.assertTrue(self.oFile.lines[13].isEndConcurrent)

        self.assertEqual(self.oFile.lines[18].line, '  O_FOO <= w_foo when (w_foo_en = \'1\') else')
        self.assertFalse(self.oFile.lines[18].isEndConcurrent)
        self.assertEqual(self.oFile.lines[19].line, ' w_bar when (w_bar_en = \'1\') else')
        self.assertTrue(self.oFile.lines[19].insideConcurrent)
        self.assertFalse(self.oFile.lines[19].isEndConcurrent)
        self.assertEqual(self.oFile.lines[20].line, ' \'Z\';')
        self.assertTrue(self.oFile.lines[20].insideConcurrent)
        self.assertTrue(self.oFile.lines[20].isEndConcurrent)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007_w_single_line_option_enabled(self):
        oRule = concurrent.rule_007()
        oRule.allow_single_line = True
        dExpected = []
        oRule.fix(self.oFile)

        self.assertEqual(self.oFile.lines[16].line, '  O_FOO <= w_foo when (w_foo_en = \'1\') else')
        self.assertFalse(self.oFile.lines[16].isEndConcurrent)
        self.assertEqual(self.oFile.lines[17].line, ' w_bar when (w_bar_en = \'1\') else')
        self.assertTrue(self.oFile.lines[17].insideConcurrent)
        self.assertFalse(self.oFile.lines[17].isEndConcurrent)
        self.assertEqual(self.oFile.lines[18].line, ' \'Z\';')
        self.assertTrue(self.oFile.lines[18].insideConcurrent)
        self.assertTrue(self.oFile.lines[18].isEndConcurrent)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
