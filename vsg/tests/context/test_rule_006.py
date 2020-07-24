
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_006_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_006_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_006(self):
        oRule = context.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '006')

        lExpected = []
        
        dViolation = utils.add_violation(9)
        dViolation['iLeftLineNumber'] = 8
        dViolation['solution'] = 'Move "is" to the right of "c1" on line 8'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(14)
        dViolation['iLeftLineNumber'] = 13
        dViolation['solution'] = 'Move "is" to the right of "c1" on line 13'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(20)
        dViolation['iLeftLineNumber'] = 19
        dViolation['solution'] = 'Move "is" to the right of "c1" on line 19'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(26)
        dViolation['iLeftLineNumber'] = 24
        dViolation['solution'] = 'Move "is" to the right of "c1" on line 24'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_006(self):
        oRule = context.rule_006()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

