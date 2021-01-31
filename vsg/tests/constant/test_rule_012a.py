
import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_012a_test_input.vhd'))

#lExpected = []
#lExpected.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_012a_test_input.fixed.vhd'), lExpected)


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012_first_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = True
        oRule.last_paren_new_line = 'Ignore'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')

        lExpected = [10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_first_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = False
        oRule.last_paren_new_line = 'Ignore'

        lExpected = [14, 17, 21, 27, 41, 57]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_last_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = True

        lExpected = [11, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_last_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = False

        lExpected = [18, 24, 38, 54, 72]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

#    def test_fix_rule_012(self):
#        oRule = constant.rule_012()
#
#        oRule.fix(self.oFile)
#
#        lActual = self.oFile.get_lines()
#
#        self.assertEqual(lExpected, lActual)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])
