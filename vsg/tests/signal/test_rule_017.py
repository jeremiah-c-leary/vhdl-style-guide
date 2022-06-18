
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

        lExpected = [3, 10, 13]

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

        lExpected = [12, 23]

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

        lExpected = [9, 20]

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
