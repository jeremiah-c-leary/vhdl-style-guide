import os

import unittest

from vsg.rules import when
from vsg import vhdlFile
from vsg.tests import utils


class testFixRuleWhenMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'when_test_input.vhd')))


    def test_rule_001(self):
        oRule = when.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'when')
        self.assertEqual(oRule.identifier, '001')

        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[13].line, '      d <= sig1 when b = \'1\' else--This is a comment')
        self.assertEqual(self.oFile.lines[14].line, '              sig2 when c = \'0\' else  -- This is a comment')
        self.assertEqual(self.oFile.lines[15].line, '              sig3 when d = \'1\' else')
        self.assertEqual(self.oFile.lines[16].line, '              sig4;')
        self.assertEqual(oRule.violations, dExpected)
