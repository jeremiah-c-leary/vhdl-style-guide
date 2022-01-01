
import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_011_test_input.vhd'))

lExpected_new_line_after_assign_yes = []
lExpected_new_line_after_assign_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_011_test_input.fixed_new_line_after_assign_yes.vhd'), lExpected_new_line_after_assign_yes)

lExpected_new_line_after_assign_no = []
lExpected_new_line_after_assign_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_011_test_input.fixed_new_line_after_assign_no.vhd'), lExpected_new_line_after_assign_no)


class test_concurrent_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_011_new_line_after_assign_yes(self):
        oRule = concurrent.rule_011()
        oRule.new_line_after_assign = 'yes'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '011')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [19, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011_new_line_after_assign_yes(self):
        oRule = concurrent.rule_011()
        oRule.new_line_after_assign = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_assign_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_011_new_line_after_assign_no(self):
        oRule = concurrent.rule_011()
        oRule.new_line_after_assign = 'no'

        lExpected = [8, 12]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011_new_line_after_assign_no(self):
        oRule = concurrent.rule_011()
        oRule.new_line_after_assign = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_assign_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
