import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))

class testFixRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)


    def test_fix_rule_001(self):
        oRule = subtype.rule_001()
        lExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
