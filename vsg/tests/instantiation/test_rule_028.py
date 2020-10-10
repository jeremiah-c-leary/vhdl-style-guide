
import os
import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_028_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_028_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_028_test_input.fixed_upper.vhd'), lExpected_upper)

class test_instantiation_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_028_lower(self):
        oRule = instantiation.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '028')

        lExpected = [27, 41]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_028_upper(self):
        oRule = instantiation.rule_028()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '028')

        lExpected = [20, 34]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_028_lower(self):
        oRule = instantiation.rule_028()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_028_upper(self):
        oRule = instantiation.rule_028()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

