
import os
import unittest

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_012_test_input.vhd'))

lExpected_1_allowed = []
lExpected_1_allowed.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_1_allowed.vhd'), lExpected_1_allowed)

lExpected_2_allowed = []
lExpected_2_allowed.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_2_allowed.vhd'), lExpected_2_allowed)


class test_whitespace_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012_1_allowed(self):
        oRule = whitespace.rule_012()
        oRule.numBlankLines = 1

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '012')

        lExpected_1_allowed = [1, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected_1_allowed, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_1_allowed(self):
        oRule = whitespace.rule_012()
        oRule.numBlankLines = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_1_allowed, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_2_allowed(self):
        oRule = whitespace.rule_012()
        oRule.numBlankLines = 2

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '012')

        lExpected_2_allowed = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected_2_allowed, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_2_allowed(self):
        oRule = whitespace.rule_012()
        oRule.numBlankLines = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_2_allowed, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

