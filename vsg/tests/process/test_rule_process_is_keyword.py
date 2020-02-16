import os

import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_is_test_input.vhd'))

class testRuleProcessIsKeyword(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_012(self):
        oRule = process.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([10,15,33])
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = process.rule_012()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[10].line, '  PROC1 : process (a, b, c) is ')
        self.assertTrue(self.oFile.lines[10].isProcessIs)
        self.assertEqual(self.oFile.lines[11].line, '')
        self.assertTrue(self.oFile.lines[11].isBlank)
        self.assertFalse(self.oFile.lines[11].isProcessIs)

        self.assertEqual(self.oFile.lines[15].line, '  PROC1 : process (a, b, c) is ')
        self.assertTrue(self.oFile.lines[15].isProcessIs)
        self.assertEqual(self.oFile.lines[16].line, '     begin')
        self.assertFalse(self.oFile.lines[16].isProcessIs)

        self.assertEqual(self.oFile.lines[33].line, '  PROC1 : process (a, b, c) is ')
        self.assertTrue(self.oFile.lines[33].isProcessIs)

        dExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
