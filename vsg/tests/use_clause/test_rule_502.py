
import os
import unittest

from vsg.rules import use_clause
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_502_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_502_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_lower_with_exceptions = []
lExpected_lower_with_exceptions.append('')
utils.read_file(os.path.join(sTestDir, 'rule_502_test_input.fixed_lower_with_exceptions.vhd'), lExpected_lower_with_exceptions)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_502_test_input.fixed_upper.vhd'), lExpected_upper)

lExpected_upper_with_exceptions = []
lExpected_upper_with_exceptions.append('')
utils.read_file(os.path.join(sTestDir, 'rule_502_test_input.fixed_upper_with_exceptions.vhd'), lExpected_upper_with_exceptions)


class test_use_clause_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_502_lower(self):
        oRule = use_clause.rule_502()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'use_clause')
        self.assertEqual(oRule.identifier, '502')

        lExpected = [4, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_502_lower_with_exceptions(self):
        oRule = use_clause.rule_502()
        oRule.case_exceptions = ['My_Math_Stuff', 'MY_LOGIC_STUFF']

        lExpected = []

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_502_upper(self):
        oRule = use_clause.rule_502()
        oRule.case = 'upper'

        lExpected = [2, 4]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_502_upper_with_exceptions(self):
        oRule = use_clause.rule_502()
        oRule.case = 'upper'
        oRule.case_exceptions = ['My_Math_Stuff', 'my_string_stuff']

        lExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_502_lower(self):
        oRule = use_clause.rule_502()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_502_lower_with_exceptions(self):
        oRule = use_clause.rule_502()
        oRule.case_exceptions = ['My_Math_Stuff', 'MY_LOGIC_STUFF']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower_with_exceptions, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_502_upper(self):
        oRule = use_clause.rule_502()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_502_upper_with_exceptions(self):
        oRule = use_clause.rule_502()
        oRule.case = 'upper'
        oRule.case_exceptions = ['My_Math_Stuff', 'my_string_stuff']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper_with_exceptions, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
