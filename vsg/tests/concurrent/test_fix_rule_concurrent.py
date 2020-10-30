import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))

class testFixRuleConcurrentMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_003(self):
        oRule = concurrent.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
