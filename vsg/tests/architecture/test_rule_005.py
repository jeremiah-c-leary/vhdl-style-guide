import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_rule_005_test_input.vhd'))

class testRuleArchitecture(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_005(self):
        oRule = architecture.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '005')

        lExpected = []

        dViolation = utils.add_violation(9,)
        dViolation['of_line'] = 10
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['of_line'] = 18
        lExpected.append(dViolation)

        dViolation = utils.add_violation(25)
        dViolation['of_line'] = 26
        lExpected.append(dViolation)

        dViolation = utils.add_violation(34)
        dViolation['of_line'] = 38
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_005(self):
        oRule = architecture.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[9].line, 'architecture rtl of')
        self.assertEqual(self.oFile.lines[10].line, '   entity1 is')

        self.assertEqual(self.oFile.lines[16].line, 'architecture rtl of')
        self.assertEqual(self.oFile.lines[18].line, '        entity1 is')

        self.assertEqual(self.oFile.lines[25].line, 'architecture rtl of')
        self.assertEqual(self.oFile.lines[26].line, 'entity1')

        self.assertEqual(self.oFile.lines[33].line, 'architecture rtl of')
        self.assertEqual(self.oFile.lines[38].line, 'entity1')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
