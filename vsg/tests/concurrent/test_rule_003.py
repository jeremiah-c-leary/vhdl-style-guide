
import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))

lExpected_align_left_no_align_paren_yes = []
lExpected_align_left_no_align_paren_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_align_left_no_align_paren_yes.vhd'), lExpected_align_left_no_align_paren_yes)

lExpected_align_left_yes_align_paren_no = []
lExpected_align_left_yes_align_paren_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_align_left_yes_align_paren_no.vhd'), lExpected_align_left_yes_align_paren_no)

lExpected_align_left_yes_align_paren_yes = []
lExpected_align_left_yes_align_paren_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_align_left_yes_align_paren_yes.vhd'), lExpected_align_left_yes_align_paren_yes)


class test_concurrent_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_003_align_left_no_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [14, 17, 20, 21, 22, 23, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_align_left_no_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_align_left_yes_align_paren_no(self):
        oRule = concurrent.rule_003()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'

        lExpected = [8, 11, 14, 17, 20, 21, 22, 23, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_align_left_yes_align_paren_no(self):
        oRule = concurrent.rule_003()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_align_left_yes_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'

        lExpected = [8, 11, 14, 17, 20, 21, 22, 23, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_align_left_yes_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
