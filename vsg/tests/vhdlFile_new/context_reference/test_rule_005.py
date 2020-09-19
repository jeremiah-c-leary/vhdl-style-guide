
import os
import unittest

from vsg.rules import context_ref
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_005_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed.vhd'), lExpected, False)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_005(self):
        self.maxDiff = None
        oRule = context_ref.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context_ref')
        self.assertEqual(oRule.identifier, '005')

        lExpected = []

        dViolation = utils.add_violation(14)
        dViolation['iObject'] = 6
        dViolation['solution'] = 'Move "context" and the code to the right to the next line.'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(18)
        dViolation['iObject'] = 5
        dViolation['solution'] = 'Move "context" and the code to the right to the next line.'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(22)
        dViolation['iObject'] = 6
        dViolation['solution'] = 'Move "context" and the code to the right to the next line.'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(31)
        dViolation['iObject'] = 4
        dViolation['solution'] = 'Move "context" and the code to the right to the next line.'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_005(self):
        oRule = context_ref.rule_005()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

