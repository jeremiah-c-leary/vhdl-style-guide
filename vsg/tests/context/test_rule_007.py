
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_007(self):
        oRule = context.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '007')

        lExpected = []

        dViolation = utils.add_violation(14)
        dViolation['solution'] = 'Move code after "is" to the next line.'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(36)
        dViolation['solution'] = 'Move code after "is" to the next line.'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(38)
        dViolation['solution'] = 'Move code after "is" to the next line.'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(40)
        dViolation['solution'] = 'Move code after "is" to the next line.'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_007(self):
        self.maxDiff = None
        oRule = context.rule_007()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

