import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleConcurrentMethods(unittest.TestCase):

    def test_rule_003(self):
        oRule = concurrent.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '003')
        dExpected = utils.add_violation_list([28,29,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
