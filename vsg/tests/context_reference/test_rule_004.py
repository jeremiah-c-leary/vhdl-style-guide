
import os
import unittest

from vsg.rules import context_ref
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_004_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_004_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_004_test_input.fixed_upper.vhd'), lExpected_upper)

class test_context_ref_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_004_lower(self):
        oRule = context_ref.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context_ref')
        self.assertEqual(oRule.identifier, '004')

        lExpected = []
        dViolation = utils.add_violation(16)
        dViolation['solution'] = 'Change "CON1" to "con1"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(17)
        dViolation['solution'] = 'Change "CON2" to "con2"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(17)
        dViolation['solution'] = 'Change "CON3" to "con3"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['solution'] = 'Change "CON2" to "con2"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['solution'] = 'Change "CON3" to "con3"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(22)
        dViolation['solution'] = 'Change "CON4" to "con4"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(29)
        dViolation['solution'] = 'Change "CON1" to "con1"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['solution'] = 'Change "Con3" to "con3"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(39)
        dViolation['solution'] = 'Change "CON1" to "con1"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(43)
        dViolation['solution'] = 'Change "Con3" to "con3"'
        lExpected.append(dViolation)


        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004_upper(self):
        oRule = context_ref.rule_004()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context_ref')
        self.assertEqual(oRule.identifier, '004')

        lExpected = []

        dViolation = utils.add_violation(6)
        dViolation['solution'] = 'Change "con1" to "CON1"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(6)
        dViolation['solution'] = 'Change "con2" to "CON2"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(6)
        dViolation['solution'] = 'Change "con3" to "CON3"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(10)
        dViolation['solution'] = 'Change "con2" to "CON2"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(10)
        dViolation['solution'] = 'Change "con3" to "CON3"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(10)
        dViolation['solution'] = 'Change "con4" to "CON4"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(31)
        dViolation['solution'] = 'Change "con2" to "CON2"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['solution'] = 'Change "Con3" to "CON3"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(41)
        dViolation['solution'] = 'Change "con2" to "CON2"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(43)
        dViolation['solution'] = 'Change "Con3" to "CON3"'
        lExpected.append(dViolation)


        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_004_lower(self):
        oRule = context_ref.rule_004()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004_upper(self):
        oRule = context_ref.rule_004()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

