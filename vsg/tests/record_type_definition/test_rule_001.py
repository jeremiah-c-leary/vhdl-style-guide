
import os
import unittest

from vsg.rules import record_type_definition
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

lExpected_new_line = []
lExpected_new_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_new_line.vhd'), lExpected_new_line, True)

lExpected_same_line = []
lExpected_same_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_same_line.vhd'), lExpected_same_line, True)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_001_same_line(self):
        oRule = record_type_definition.rule_001()
        oRule.action = 'same_line'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'record_type_definition')
        self.assertEqual(oRule.identifier, '001')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [7]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_same_line(self):
        oRule = record_type_definition.rule_001()
        oRule.action = 'same_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_same_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_001_new_line(self):
        oRule = record_type_definition.rule_001()
        oRule.action = 'new_line'

        lExpected = [4]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_new_line(self):
        oRule = record_type_definition.rule_001()
        oRule.action = 'new_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

