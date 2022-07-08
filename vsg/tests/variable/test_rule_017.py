
import os
import unittest

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_017_test_input.vhd'))

lExpected_record_constraint_open_paren__add_new_line = []
lExpected_record_constraint_open_paren__add_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_open_paren__add_new_line.vhd'), lExpected_record_constraint_open_paren__add_new_line)

lExpected_record_constraint_open_paren__remove_new_line = []
lExpected_record_constraint_open_paren__remove_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_open_paren__remove_new_line.vhd'), lExpected_record_constraint_open_paren__remove_new_line)

lExpected_record_constraint_close_paren__add_new_line = []
lExpected_record_constraint_close_paren__add_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_close_paren__add_new_line.vhd'), lExpected_record_constraint_close_paren__add_new_line)

lExpected_record_constraint_close_paren__remove_new_line = []
lExpected_record_constraint_close_paren__remove_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_close_paren__remove_new_line.vhd'), lExpected_record_constraint_close_paren__remove_new_line)

lExpected_record_constraint_comma__remove_new_line = []
lExpected_record_constraint_comma__remove_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_comma__remove_new_line.vhd'), lExpected_record_constraint_comma__remove_new_line)

lExpected_record_constraint_element__add_new_line = []
lExpected_record_constraint_element__add_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_element__add_new_line.vhd'), lExpected_record_constraint_element__add_new_line)

lExpected_record_constraint_element__remove_new_line = []
lExpected_record_constraint_element__remove_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_record_constraint_element__remove_new_line.vhd'), lExpected_record_constraint_element__remove_new_line)

lExpected_array_constraint__all_in_one_line = []
lExpected_array_constraint__all_in_one_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_array_constraint__all_in_one_line.vhd'), lExpected_array_constraint__all_in_one_line)

lExpected_array_constraint__one_line_per_dimension = []
lExpected_array_constraint__one_line_per_dimension.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_array_constraint__one_line_per_dimension.vhd'), lExpected_array_constraint__one_line_per_dimension)

lExpected_exception__one = []
lExpected_exception__one.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed_exception__one.vhd'), lExpected_exception__one)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_017_record_constraint_open_paren__add_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'add_new_line'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [3, 11, 12, 25, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_open_paren__add_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'add_new_line'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_open_paren__add_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_record_constraint_open_paren__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'remove_new_line'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_open_paren__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'remove_new_line'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_open_paren__remove_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_record_constraint_close_paren__add_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'add_new_line'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [11, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_close_paren__add_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'add_new_line'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_close_paren__add_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_record_constraint_close_paren__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'remove_new_line'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [10, 20, 29]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_close_paren__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'remove_new_line'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_close_paren__remove_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_record_constraint_comma__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'remove_new_line'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [8, 18]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_comma__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'remove_new_line'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_comma__remove_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_record_constraint_element__add_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'add_new_line'
        oRule.array_constraint = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [11, 11, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_element__add_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'add_new_line'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_element__add_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_record_constraint_element__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'remove_new_line'
        oRule.array_constraint = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [4, 5, 7, 9, 11, 12, 13, 19, 21, 23, 28]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_element__remove_new_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'remove_new_line'
        oRule.array_constraint = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_record_constraint_element__remove_new_line , lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_array_constraint__all_in_one_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'all_in_one_line'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [14, 16, 21]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_array_constraint__all_in_one_line(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'all_in_one_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_array_constraint__all_in_one_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_array_constraint__one_line_per_dimension(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'one_line_per_dimension'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [4, 5, 5, 7, 9, 11, 11, 11, 14, 16, 19, 21, 23, 25, 28]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_array_constraint__one_line_per_dimension(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'one_line_per_dimension'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_array_constraint__one_line_per_dimension, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_exception_one(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'add_new_line'
        oRule.record_constraint_close_paren = 'add_new_line'
        oRule.record_constraint_comma = 'remove_new_line'
        oRule.record_constraint_element = 'add_new_line'
        oRule.array_constraint = 'all_in_one_line'
        oRule.exceptions.append('keep_record_constraint_with_single_element_on_one_line')

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [3, 8, 11, 11, 11, 11, 12, 14, 16, 18, 21, 23, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_exception__one(self):
        oRule = variable.rule_017()
        oRule.record_constraint_open_paren = 'add_new_line'
        oRule.record_constraint_close_paren = 'add_new_line'
        oRule.record_constraint_comma = 'remove_new_line'
        oRule.record_constraint_element = 'add_new_line'
        oRule.array_constraint = 'all_in_one_line'
        oRule.exceptions.append('keep_record_constraint_with_single_element_on_one_line')

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_exception__one, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

