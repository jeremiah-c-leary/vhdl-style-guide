import os
import unittest

from vsg.rules import length
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'length_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleLengthMethods(unittest.TestCase):

    def test_rule_001_with_default(self):
        oRule = length.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'length')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [3,7,9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001_with_75_character_limit(self):
        oRule = length.rule_001()
        oRule.length = 75
        dExpected = [1,3,4,7,9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

