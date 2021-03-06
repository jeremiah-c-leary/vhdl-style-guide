
import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_009_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed.vhd'), lExpected)

lExpected_align_left_yes_align_paren_no = []
lExpected_align_left_yes_align_paren_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no.vhd'), lExpected_align_left_yes_align_paren_no)

lExpected_align_left_no_align_paren_no = []
lExpected_align_left_no_align_paren_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no.vhd'), lExpected_align_left_no_align_paren_no)

lExpected_align_left_no_align_paren_yes_wrap_at_when_yes = []
lExpected_align_left_no_align_paren_yes_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_wrap_at_when_yes.vhd'), lExpected_align_left_no_align_paren_yes_wrap_at_when_yes)


class test_concurrent_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    @unittest.skip('Yes')
    def test_rule_009(self):
        oRule = concurrent.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '009')

        lExpected = [46, 49, 53, 54, 57, 58, 59, 60, 63, 64, 65, 66, 67]
        lExpected.extend(range(70, 75))
        lExpected.extend(range(77, 80))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Yes')
    def test_fix_rule_009(self):
        oRule = concurrent.rule_009()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


    def test_fix_rule_009_align_left_yes_align_paren_no(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.wrap_condition_at_when = 'no'
        oRule.align_when_keywords = 'no'
        oRule.align_else_keywords = 'no'
        oRule.align_paren = 'no'
        oRule.ignore_single_line = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.wrap_condition_at_when = 'no'
        oRule.align_when_keywords = 'no'
        oRule.align_else_keywords = 'no'
        oRule.align_paren = 'no'
        oRule.ignore_single_line = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.align_else_keywords = 'no'
        oRule.align_paren = 'no'
        oRule.ignore_single_line = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

