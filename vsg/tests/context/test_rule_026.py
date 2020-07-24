
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_026_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_026(self):
        oRule = context.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '026')

        lExpected = []
        dViolation = utils.add_violation(7)
        dViolation['iRemove'] = 1
        lExpected.append(dViolation)
 
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

        self.assertEqual('Remove all but one blank line below this line.', oRule._get_solution(7))

    def test_fix_rule_026(self):
        oRule = context.rule_026()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

