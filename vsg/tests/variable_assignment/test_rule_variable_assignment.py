import os
import unittest

from vsg.rules import variable_assignment
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable_assignment','variable_assignment_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleVariableAssignmentMethods(unittest.TestCase):

    def test_rule_004(self):
        oRule = variable_assignment.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable_assignment')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([54,55,74])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

