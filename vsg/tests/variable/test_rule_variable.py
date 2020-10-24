import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleVariableMethods(unittest.TestCase):


    def test_rule_007(self):
        oRule = variable.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '007')
        dExpected = utils.add_violation_list([11,16])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
