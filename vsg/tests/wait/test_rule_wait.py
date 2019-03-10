import os

import unittest

from vsg.rules import wait
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','wait','wait_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleProcessMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = wait.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'wait')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [34,36]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
