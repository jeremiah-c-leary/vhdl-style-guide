import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentCase(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_011(self):
        oRule = variable.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [16, 18, 19, 21]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = variable.rule_011()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[16].line, '    var1 <= \'0\';')
        self.assertEqual(self.oFile.lines[18].line, '    if (var2 = \'0\') then')
        self.assertEqual(self.oFile.lines[19].line, '      var3 <= \'1\';')
        self.assertEqual(self.oFile.lines[21].line, '      var4 <= \'0\';')

        self.assertEqual(oRule.violations, [])
