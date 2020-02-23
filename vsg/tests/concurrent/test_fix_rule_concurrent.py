import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))

class testFixRuleConcurrentMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = concurrent.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = concurrent.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = concurrent.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = concurrent.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = concurrent.rule_005()
        dExpected = []
        oRule.fix(self.oFile)

        self.assertEqual(self.oFile.lines[32].line, 'a<=b;')
        self.assertFalse(self.oFile.lines[32].hasConcurrentLabel)

        self.assertEqual(self.oFile.lines[33].line, ' a<=b;')
        self.assertFalse(self.oFile.lines[33].hasConcurrentLabel)

        self.assertEqual(self.oFile.lines[34].line, '  a <= b;  -- this else should not trigger')
        self.assertFalse(self.oFile.lines[34].hasConcurrentLabel)

        self.assertEqual(self.oFile.lines[35].line, '  a <= b or c')
        self.assertFalse(self.oFile.lines[35].hasConcurrentLabel)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = concurrent.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = concurrent.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[34].line, '  label : a <= b;  -- this else should not trigger')
        self.assertEqual(self.oFile.lines[49].line, '  a <= b when g = \'1\' else')
        self.assertFalse(self.oFile.lines[49].hasComment)
        self.assertFalse(self.oFile.lines[49].hasInlineComment)
        self.assertEqual(self.oFile.lines[49].commentColumn, None)
        self.assertFalse(self.oFile.lines[49].isEndConcurrent)
        self.assertTrue(self.oFile.lines[49].isConcurrentBegin)
        self.assertEqual(self.oFile.lines[50].line, ' \'1\'; -- Not an error')
        self.assertTrue(self.oFile.lines[50].hasComment)
        self.assertTrue(self.oFile.lines[50].hasInlineComment)
        self.assertEqual(self.oFile.lines[50].commentColumn, 6)
        self.assertTrue(self.oFile.lines[50].isEndConcurrent)
        self.assertFalse(self.oFile.lines[50].isConcurrentBegin)

    def test_fix_rule_008(self):
        oRule = concurrent.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
