import os

import unittest
from vsg.rules import wait 
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'wait_test_input.vhd'))


class testFixRuleProcessMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = wait.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[34].line, '    wait for 10ns;')
        self.assertEqual(oFile.lines[35].line, '    wait on a,b;')
        self.assertEqual(oFile.lines[36].line, '    wait until a = \'0\';')
