import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import general
from vsg import vhdlFile
from vsg.tests import utils


class testGeneralRule(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'general_001_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = general.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'general')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [9, 12, 14, 15, 16, 17]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
