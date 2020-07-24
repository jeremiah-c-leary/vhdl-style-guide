
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_005_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_005_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_005(self):
        self.maxDiff = None
        oRule = context.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '005')

        lExpected = []
        
        dViolation = utils.add_violation(9)
        dViolation['iLeftLineNumber'] = 8
        dViolation['solution'] = 'Move "c1" to the right of "context" on line 8'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(13)
        dViolation['iLeftLineNumber'] = 12
        dViolation['solution'] = 'Move "c1" to the right of "context" on line 12'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(19)
        dViolation['iLeftLineNumber'] = 18
        dViolation['solution'] = 'Move "c1" to the right of "context" on line 18'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(25)
        dViolation['iLeftLineNumber'] = 24
        dViolation['solution'] = 'Move "c1" to the right of "context" on line 24'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_005(self):
        oRule = context.rule_005()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

