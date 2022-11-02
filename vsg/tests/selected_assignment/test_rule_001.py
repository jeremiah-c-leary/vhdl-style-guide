
import os
import unittest

from vsg.rules import selected_assignment
from vsg import vhdlFile
from vsg.tests import utils
from vsg import config

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

lExpected_new_line_after_while_no = []
lExpected_new_line_after_while_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_after_while_no.vhd'), lExpected_new_line_after_while_no, False)

lExpected_new_line_after_while_yes = []
lExpected_new_line_after_while_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_after_while_yes.vhd'), lExpected_new_line_after_while_yes, False)

lExpected_new_line_after_select_keyword_no = []
lExpected_new_line_after_select_keyword_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_after_select_keyword_no.vhd'), lExpected_new_line_after_select_keyword_no, False)

lExpected_new_line_after_select_keyword_yes = []
lExpected_new_line_after_select_keyword_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_after_select_keyword_yes.vhd'), lExpected_new_line_after_select_keyword_yes, False)

lExpected_new_line_before_select_keyword_no = []
lExpected_new_line_before_select_keyword_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_before_select_keyword_no.vhd'), lExpected_new_line_before_select_keyword_no, False)

lExpected_new_line_before_select_keyword_yes = []
lExpected_new_line_before_select_keyword_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_before_select_keyword_yes.vhd'), lExpected_new_line_before_select_keyword_yes, False)

lExpected_new_line_before_when_keyword_yes = []
lExpected_new_line_before_when_keyword_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line_before_when_keyword_yes.vhd'), lExpected_new_line_before_when_keyword_yes, False)

lExpected_single_line_with_expression_yes = []
lExpected_single_line_with_expression_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_single_line_with_expression_yes.vhd'), lExpected_single_line_with_expression_yes, False)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oRule = selected_assignment.rule_001()
        self.oConfig = config.config()
        self.dConfig = {}
        self.dConfig['rule'] = {}
        self.dConfig['rule']['selected_assignment_001'] = {}
        self.dConfig['rule']['selected_assignment_001']['new_line_after_with_keyword'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_before_select_keyword'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_after_select_keyword'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_before_assignment'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_after_assignment'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_before_when_keyword'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_after_when_keyword'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_before_comma'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_after_comma'] = 'ignore'
        self.dConfig['rule']['selected_assignment_001']['new_line_before_semicolon'] = 'ignore'

        self.dConfig['rule']['selected_assignment_001']['single_line_with_expression'] = 'ignore'

    def test_rule_001_new_line_after_with_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_with_keyword'] = 'no'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [52, 72, 94, 117]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_new_line_after_with_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_with_keyword'] = 'no'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_while_no, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

    def test_rule_001_new_line_after_with_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_with_keyword'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [10, 15, 20, 27, 37, 39, 41, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_new_line_after_with_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_with_keyword'] = 'yes'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_while_yes, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

    def test_rule_001_new_line_after_with_keyword_ignore(self):

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = []

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_select_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_select_keyword'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [10, 15, 20, 27, 56, 77, 99, 121]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_new_line_after_select_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_select_keyword'] = 'no'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_select_keyword_no, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

    def test_rule_001_new_line_after_select_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_select_keyword'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [37, 39, 41, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_new_line_after_select_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_select_keyword'] = 'yes'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_select_keyword_yes, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

    def test_rule_001_new_line_before_select_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_select_keyword'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [56, 77, 99, 121]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_new_line_before_select_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_select_keyword'] = 'no'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_before_select_keyword_no, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

    def test_rule_001_new_line_before_select_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_select_keyword'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [10, 15, 20, 27, 37, 39, 41, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_new_line_before_select_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_select_keyword'] = 'yes'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_before_select_keyword_yes, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

    def test_rule_001_new_line_before_assignment_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_assignment'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [58, 79, 101, 123]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_assignment_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_assignment'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [11, 16, 21, 28, 37, 39, 41, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_assignment_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_assignment'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [58, 79, 101, 123]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_assignment_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_assignment'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [11, 16, 21, 28, 37, 39, 41, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_when_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_when_keyword'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [60, 64, 68, 82, 86, 90, 103, 107, 111, 126, 130, 134]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_when_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_when_keyword'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [11, 12, 13, 16, 17, 18, 21, 22, 23, 28, 29, 30, 37, 37, 37, 39, 39, 39, 41, 41, 41, 45, 45, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_when_keyword_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_when_keyword'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [60, 64, 68, 82, 86, 90, 103, 107, 111, 126, 130, 134]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_when_keyword_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_when_keyword'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [11, 12, 13, 16, 17, 18, 21, 22, 23, 28, 29, 30, 37, 37, 37, 39, 39, 39, 41, 41, 41, 45, 45, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_comma_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_comma'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [62, 66, 84, 88, 105, 109, 128, 132]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_comma_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_comma'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [11, 12, 16, 17, 21, 22, 28, 29, 37, 37, 39, 39, 41, 41, 45, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_comma_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_comma'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [11, 12, 16, 17, 21, 22, 28, 29, 62, 66, 84, 88, 105, 109, 128, 132]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_after_comma_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_after_comma'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [37, 37, 39, 39, 41, 41, 45, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_semicolon_no(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_semicolon'] = 'no'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [70, 92, 113, 136]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_rule_001_new_line_before_semicolon_yes(self):

        self.dConfig['rule']['selected_assignment_001']['new_line_before_semicolon'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [13, 18, 23, 30, 37, 39, 41, 45]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))





    def test_rule_001_single_line_with_expression_yes(self):

        self.dConfig['rule']['selected_assignment_001']['single_line_with_expression'] = 'yes'

        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.assertTrue(self.oRule)
        self.assertEqual(self.oRule.name, 'selected_assignment')
        self.assertEqual(self.oRule.identifier, '001')

        lExpected = [53, 73, 95, 118]

        self.oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(self.oRule.violations))

    def test_fix_rule_001_single_line_with_expression_yes(self):

        self.dConfig['rule']['selected_assignment_001']['single_line_with_expression'] = 'yes'
        self.oConfig.dConfig = self.dConfig
        self.oRule.configure(self.oConfig)

        self.oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_single_line_with_expression_yes, lActual)

        self.oRule.analyze(self.oFile)
        self.assertEqual(self.oRule.violations, [])

