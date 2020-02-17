import unittest
import sys
sys.path.append('vsg')

from vsg.rules import source_file
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile('no_file.vhd')
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSignalMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = source_file.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'source_file')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [utils.add_violation(0)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
