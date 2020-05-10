import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generate_2008_test_input.vhd'))

class testRuleGenerateMethods(unittest.TestCase):

    def setUp(self):
       self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_016(self):
        oRule = generate.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '016')

        lExpected = utils.add_violation_list([9,19])

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_016(self):
        oRule = generate.rule_016()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile) 

        self.assertEqual(self.oFile.lines[9].line,'    when 0 =>')
        self.assertEqual(self.oFile.lines[11].line,'    when 1 =>')
        self.assertEqual(self.oFile.lines[19].line,'    when others =>')

        self.assertEqual(oRule.violations, [])
