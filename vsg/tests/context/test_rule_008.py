
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_008_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_008_test_input.fixed.vhd'), lExpected, False)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_008(self):
        oRule = context.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '008')

        lExpected = []
        dViolation = utils.add_violation(9)
        dViolation['iObject'] = 6
        lExpected.append(dViolation)

        dViolation = utils.add_violation(13)
        dViolation['iObject'] = 7
        lExpected.append(dViolation)

        dViolation = utils.add_violation(20)
        dViolation['iObject'] = 6
        lExpected.append(dViolation)

        dViolation = utils.add_violation(26)
        dViolation['iObject'] = 6
        lExpected.append(dViolation)

        dViolation = utils.add_violation(31)
        dViolation['iObject'] = 16
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['iObject'] = 16
        lExpected.append(dViolation)

        dViolation = utils.add_violation(35)
        dViolation['iObject'] = 16
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_008(self):
        self.maxDiff = None
        oRule = context.rule_008()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

