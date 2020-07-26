
import os
import unittest

from vsg.rules import context_ref
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed.vhd'), lExpected)


class test_context_ref_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = context_ref.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context_ref')
        self.assertEqual(oRule.identifier, '001')

        lExpected = []
        dViolation = utils.add_violation(11)
        dViolation['action'] = 'insert'
        dViolation['solution'] = 'Indent 4 spaces'
        dViolation['iSpaces'] = '    '
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['action'] = 'change'
        dViolation['solution'] = 'Indent 4 spaces'
        dViolation['iSpaces'] = '    '
        lExpected.append(dViolation)

        dViolation = utils.add_violation(35)
        dViolation['action'] = 'insert'
        dViolation['solution'] = 'Indent 4 spaces'
        dViolation['iSpaces'] = '    '
        lExpected.append(dViolation)

        dViolation = utils.add_violation(45)
        dViolation['action'] = 'insert'
        dViolation['solution'] = 'Indent 2 spaces'
        dViolation['iSpaces'] = '  '
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, oRule.violations)

        self.assertEqual(oRule._get_solution(11),'Indent 4 spaces')
        self.assertEqual(oRule._get_solution(45),'Indent 2 spaces')

    def test_fix_rule_001(self):
        self.maxDiff = None
        oRule = context_ref.rule_001()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

