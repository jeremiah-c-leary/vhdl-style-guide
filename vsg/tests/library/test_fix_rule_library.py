import os

import unittest

from vsg.rules import library
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd'))

class testFixRuleLibraryMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = library.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = library.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = library.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = library.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = library.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = library.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = library.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = library.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
