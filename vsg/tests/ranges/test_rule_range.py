import os
import unittest

from vsg.rules import ranges
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'range_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleRange(unittest.TestCase):

    def test_rule_001_with_default(self):
        oRule = ranges.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'range')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [{'line_number': 17, 'words_to_fix': {'downTo'}},
                     {'line_number': 21, 'words_to_fix': {'Downto'}},
                     {'line_number': 28, 'words_to_fix': {'DOWNTO'}},
                     {'line_number': 33, 'words_to_fix': {'dOWnto'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001_with_uppercase(self):
        oRule = ranges.rule_001()
        oRule.case = 'upper'
        dExpected = [{'line_number': 5, 'words_to_fix': {'downto'}},
                     {'line_number': 9, 'words_to_fix': {'downto'}},
                     {'line_number': 17, 'words_to_fix': {'downTo'}},
                     {'line_number': 21, 'words_to_fix': {'Downto'}},
                     {'line_number': 29, 'words_to_fix': {'downto'}},
                     {'line_number': 33, 'words_to_fix': {'dOWnto'}},
                     {'line_number': 34, 'words_to_fix': {'downto'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_with_default(self):
        oRule = ranges.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'range')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [{'line_number': 18, 'words_to_fix': {'TO'}},
                     {'line_number': 22, 'words_to_fix': {'tO'}},
                     {'line_number': 30, 'words_to_fix': {'To'}},
                     {'line_number': 35, 'words_to_fix': {'TO'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_with_uppercase(self):
        oRule = ranges.rule_002()
        oRule.case = 'upper'
        dExpected = [{'line_number': 6, 'words_to_fix': {'to'}},
                     {'line_number': 10, 'words_to_fix': {'to'}},
                     {'line_number': 22, 'words_to_fix': {'tO'}},
                     {'line_number': 30, 'words_to_fix': {'To'}},
                     {'line_number': 31, 'words_to_fix': {'to'}},
                     {'line_number': 36, 'words_to_fix': {'to'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
