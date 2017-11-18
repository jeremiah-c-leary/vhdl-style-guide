import os

import unittest
import sys
import copy

from vsg.rules import port
from vsg import vhdlFile


oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))


class testRulePortMethods(unittest.TestCase):


    def test_fix_rule_002(self):
        oRule = port.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])


if __name__ == '__main__':
    unittest.main()
