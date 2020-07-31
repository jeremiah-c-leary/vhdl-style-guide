
import os
import unittest

from vsg.rules import context_ref
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_upper.vhd'), lExpected_upper)

class test_context_ref_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_003_lower(self):
        oRule = context_ref.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context_ref')
        self.assertEqual(oRule.identifier, '003')

        lExpected = []
        dViolation = utils.add_violation(16)
        dViolation['solution'] = 'Change "CONTEXT" to "context"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(20)
        dViolation['solution'] = 'Change "CONTEXT" to "context"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['solution'] = 'Change "conTEXT" to "context"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['solution'] = 'Change "CoNtExT" to "context"'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003_upper(self):
        oRule = context_ref.rule_003()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context_ref')
        self.assertEqual(oRule.identifier, '003')

        lExpected = []

        dViolation = utils.add_violation(6)
        dViolation['solution'] = 'Change "context" to "CONTEXT"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(10)
        dViolation['solution'] = 'Change "context" to "CONTEXT"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['solution'] = 'Change "conTEXT" to "CONTEXT"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['solution'] = 'Change "CoNtExT" to "CONTEXT"'
        lExpected.append(dViolation)


        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_003_lower(self):
        oRule = context_ref.rule_003()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003_upper(self):
        oRule = context_ref.rule_003()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

