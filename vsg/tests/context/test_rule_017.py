
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_017_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_017_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_017(self):
        oRule = context.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '017')

        lExpected = []

        dViolation = utils.add_violation(8)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "c1" and "is"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(12)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "c1" and "is"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(17)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "c1" and "is"'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_017(self):
        oRule = context.rule_017()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

