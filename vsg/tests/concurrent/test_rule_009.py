
import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_009_test_input.vhd'))

#00000
lExpected_align_left_no = []
lExpected_align_left_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no.vhd'), lExpected_align_left_no)

#00001
lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes = []
lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes)

#00010
lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes = []
lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes)

#00011
lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes)

#00100
lExpected_align_left_no_align_paren_no_align_when_yes = []
lExpected_align_left_no_align_paren_no_align_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_yes)

#00101
lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes = []
lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes)

#00110
lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes = []
lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes)

#00111
lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes)

#01000
lExpected_align_left_no_align_paren_yes = []
lExpected_align_left_no_align_paren_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes.vhd'), lExpected_align_left_no_align_paren_yes)

#01001
lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes = []
lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes)

#01010
lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes = []
lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes)

#01011
lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes)

#01100
lExpected_align_left_no_align_paren_yes_align_when_yes = []
lExpected_align_left_no_align_paren_yes_align_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_yes)

#01101
lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes = []
lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes)

#01110
lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes = []
lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes)

#01111
lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes)

#10000
lExpected_align_left_yes = []
lExpected_align_left_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes.vhd'), lExpected_align_left_yes)

#10001
lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes = []
lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes)

#10010
lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes = []
lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes)

#10011
lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes)

#10100
lExpected_align_left_yes_align_paren_no_align_when_yes = []
lExpected_align_left_yes_align_paren_no_align_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_yes)

#10101
lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes = []
lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes)

#10110
lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes = []
lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes)

#10111
lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes)

#11000
lExpected_align_left_yes_align_paren_yes = []
lExpected_align_left_yes_align_paren_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes.vhd'), lExpected_align_left_yes_align_paren_yes)

#11001
lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes)

#11010
lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes)

#11011
lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes)

#11100
lExpected_align_left_yes_align_paren_yes_align_when_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_yes)

#11101
lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes)

#11110
lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes)

#11111
lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes = []
lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes.vhd'), lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes)


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

    def test_fix_rule_009_align_left_no(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(oRule.groups, ['alignment'])
        self.assertEqual(lExpected_align_left_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_when_keywords = 'no'
        oRule.align_else_keywords = 'no'
        oRule.align_paren = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_no_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no_align_when_yes_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_no_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_no_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes(self):
        oRule = concurrent.rule_009()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'yes'
        oRule.align_else_keywords = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes_align_when_yes_wrap_at_when_yes_align_else_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

