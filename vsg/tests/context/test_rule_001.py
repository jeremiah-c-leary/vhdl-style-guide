
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = context.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '001')

        lExpected = []
        dViolation = utils.add_violation(8)
        dViolation['action'] = 'remove'
        dViolation['solution'] = 'Remove spaces before "context"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(17)
        dViolation['action'] = 'remove'
        dViolation['solution'] = 'Remove spaces before "context"'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

        self.assertEqual(oRule._get_solution(8),'Remove spaces before "context"')
        self.assertEqual(oRule._get_solution(17),'Remove spaces before "context"')

    def test_fix_rule_001(self):
        oRule = context.rule_001()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

