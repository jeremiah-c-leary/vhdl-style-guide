
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_009_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_009_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_009(self):
        oRule = context.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '009')

        lExpected = []
        
        dViolation = utils.add_violation(10)
        dViolation['iLeftLineNumber'] = 9
        dViolation['solution'] = 'Move "context" to the right of "end" on line 9'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(18)
        dViolation['iLeftLineNumber'] = 16
        dViolation['solution'] = 'Move "context" to the right of "end" on line 16'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['iLeftLineNumber'] = 23
        dViolation['solution'] = 'Move "context" to the right of "end" on line 23'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(34)
        dViolation['iLeftLineNumber'] = 31
        dViolation['solution'] = 'Move "context" to the right of "end" on line 31'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_009(self):
        self.maxDiff = None
        oRule = context.rule_009()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

