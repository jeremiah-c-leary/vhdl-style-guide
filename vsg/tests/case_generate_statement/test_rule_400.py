
import os
import unittest

from vsg.rules import case_generate_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_400_test_input.vhd'))

lExpected_true = []
lExpected_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed_compact_alignment__true.vhd'), lExpected_true)


class test_case_generate_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400_true(self):
        oRule = case_generate_statement.rule_400()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case_generate_statement')
        self.assertEqual(oRule.identifier, '400')
        self.assertTrue(oRule.compact_alignment)
        self.assertFalse(oRule.blank_line_ends_group)
        self.assertFalse(oRule.comment_line_ends_group)
        self.assertFalse(oRule.separate_generic_port_alignment)

        lExpected = [8, 10]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_400_true(self):
        oRule = case_generate_statement.rule_400()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

