import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generate','generate_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleGenerateMethods(unittest.TestCase):

    def test_rule_015(self):
        oRule = generate.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [utils.add_violation(104)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
