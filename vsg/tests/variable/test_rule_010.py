
import os
import unittest

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_010_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_010_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_010_test_input.fixed_upper.vhd'), lExpected_upper)

class test_variable_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_010_lower(self):
        oRule = variable.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '010')
        self.assertEqual(oRule.groups, ['case', 'case::name'])

        lExpected = [21, 22, 27, 28]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_010_upper(self):
        oRule = variable.rule_010()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '010')

        lExpected = [4, 5, 10, 11]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_010_lower(self):
        oRule = variable.rule_010()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010_upper(self):
        oRule = variable.rule_010()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

