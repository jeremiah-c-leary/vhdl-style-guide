
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_022_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_022_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_022(self):
        oRule = context.rule_022()
        oRule.insert_space = True
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '022')

        lExpected = []

        dViolation = utils.add_violation(9)
        dViolation['copy_value'] = 'con2'
        dViolation['solution'] = 'Add "con2" after "context"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(27)
        dViolation['copy_value'] = 'con5'
        dViolation['solution'] = 'Add "con5" after "context"'
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

        self.assertEqual('Add "con2" after "context"', oRule._get_solution(9))

    def test_fix_rule_022(self):
        oRule = context.rule_022()
        oRule.insert_space = True

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

