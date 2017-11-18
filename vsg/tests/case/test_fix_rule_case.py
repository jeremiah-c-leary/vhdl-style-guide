import os
import unittest

from vsg.rules import case
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','case','case_test_input.vhd'))
oFileSequential = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','case','case_sequential_test_input.vhd'))

class testRuleConcurrentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = case.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])


if __name__ == '__main__':
    unittest.main()
