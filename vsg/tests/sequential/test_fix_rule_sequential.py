import os
import unittest
import sys
#sys.path.append('vsg')

from vsg.rules import sequential
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','sequential','sequential_test_input.vhd'))

class testRuleSequentialMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = sequential.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
