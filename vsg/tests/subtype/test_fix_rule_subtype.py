import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile) 

class testFixRuleSignalMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = subtype.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
