import os

import unittest

from vsg.rules import when
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests

oFile = vhdlFile.vhdlFile(utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'when_test_input.vhd')))

class testRuleWhenMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = when.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'when')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [14,15,16]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
