
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_012_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_upper.vhd'), lExpected_upper)

class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_012_lower(self):
        oRule = context.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '012')

        lExpected = []
        dViolation = utils.add_violation(3)
        dViolation['solution'] = 'Change "CON1" to "con1"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(11)
        dViolation['solution'] = 'Change "Co1" to "co1"'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_012_upper(self):
        oRule = context.rule_012()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '012')

        lExpected = []

        dViolation = utils.add_violation(8)
        dViolation['solution'] = 'Change "con1" to "CON1"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(11)
        dViolation['solution'] = 'Change "Co1" to "CO1"'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_012_lower(self):
        oRule = context.rule_012()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_upper(self):
        oRule = context.rule_012()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

