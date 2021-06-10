
import os
import unittest

from vsg.rules import sequential
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_005_test_input.vhd'))

lExpected_all = []
lExpected_all.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed.vhd'), lExpected_all)

lExpected_blank_if = []
lExpected_blank_if.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed_allowing_blank_and_if.vhd'), lExpected_blank_if)

lExpected_blank_if_case = []
lExpected_blank_if_case.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed_allowing_blank_and_if_and_case.vhd'), lExpected_blank_if_case)

lExpected_blank_case = []
lExpected_blank_case.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed_allowing_blank_and_case.vhd'), lExpected_blank_case)

lExpected_blank_when = []
lExpected_blank_when.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed_allowing_blank_and_when.vhd'), lExpected_blank_when)

class test_sequential_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_005(self):
        oRule = sequential.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '005')

        lExpected = [48, 49, 50, 53, 54, 55, 57, 58, 66, 67, 68]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_005_allowing_blank_and_if(self):
        oRule = sequential.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '005')

        oRule.if_control_statements_ends_group = False
        oRule.blank_line_ends_group = False

        lExpected = [9, 10, 11, 14, 15, 16, 18, 19, 20, 48, 49, 50, 53, 54, 55, 57, 58, 66, 67, 68]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_005_allowing_blank_and_case(self):
        oRule = sequential.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '005')

        oRule.case_control_statements_ends_group = False
        oRule.blank_line_ends_group = False

        lExpected = [31, 32, 33, 35, 36, 37, 48, 49, 50, 53, 54, 55, 57, 58, 66, 67, 68]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_005_allowing_blank_and_when(self):
        oRule = sequential.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '005')

        oRule.case_control_statements_ends_group = False
        oRule.case_keyword_statements_ends_group = True
        oRule.blank_line_ends_group = False

        lExpected = [31, 32, 33, 48, 49, 50, 53, 54, 55, 57, 58, 66, 67, 68]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_005_allowing_blank_and_if_and_case(self):
        oRule = sequential.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '005')

        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False
        oRule.blank_line_ends_group = False

        lExpected = [9, 10, 11, 14, 15, 16, 18, 19, 20, 31, 32, 33, 35, 36, 37, 48, 49, 50, 53, 54, 55, 57, 58, 66, 67, 68]

        oRule.analyze(self.oFile), 
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_005(self):
        oRule = sequential.rule_005()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005_allowing_blank_and_if(self):
        oRule = sequential.rule_005()

        oRule.if_control_statements_ends_group = False
        oRule.blank_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_blank_if, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005_allowing_blank_and_if_and_case(self):
        oRule = sequential.rule_005()

        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False
        oRule.blank_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_blank_if_case, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005_allowing_blank_and_case(self):
        oRule = sequential.rule_005()

        oRule.case_control_statements_ends_group = False
        oRule.blank_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_blank_case, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005_allowing_blank_and_when(self):
        oRule = sequential.rule_005()

        oRule.case_control_statements_ends_group = False
        oRule.case_keyword_statements_ends_group = True
        oRule.blank_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_blank_when, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

