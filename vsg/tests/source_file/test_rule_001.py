import unittest
import sys
sys.path.append('vsg')

from vsg.rules import source_file
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile('no_file.vhd')

class testRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = source_file.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'source_file')
        self.assertEqual(oRule.identifier, '001')

        lExpected = [0]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

