
import os
import unittest

from vsg.rules import signal
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


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_017_record_constraint_open_paren__add_new_line(self):
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'add_new_line'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [3, 11, 12]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_open_paren__add_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'remove_new_line'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_open_paren__remove_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'add_new_line'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [11, 23]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_close_paren__add_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'remove_new_line'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [10, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_close_paren__remove_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'remove_new_line'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [8, 18]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_comma__remove_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'add_new_line'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [11, 11]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_element__add_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'remove_new_line'
        oRule.array_constraint = 'ignore'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [4, 5, 7, 9, 11, 12, 13, 19, 21, 23]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_record_constraint_element__remove_new_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'all_in_one_line'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [14, 16, 21]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_array_constraint__all_in_one_line(self):
        oRule = signal.rule_017()
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
        oRule = signal.rule_017()
        oRule.record_constraint_open_paren = 'ignore'
        oRule.record_constraint_close_paren = 'ignore'
        oRule.record_constraint_comma = 'ignore'
        oRule.record_constraint_element = 'ignore'
        oRule.array_constraint = 'one_line_per_dimension'

        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [4, 5, 5, 7, 8, 11, 11, 11, 14, 17, 19, 21, 23]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_array_constraint__one_line_per_dimension(self):
        oRule = signal.rule_017()
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

