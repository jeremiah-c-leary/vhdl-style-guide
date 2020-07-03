import os
import unittest

from vsg.rules import semicolon
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'rule_001_test_input.vhd'))

class testRuleSemiColon(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)


    def test_rule_001(self):
        oRule = semicolon.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'semicolon')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([6,7,9,11,13,21])
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

        self.assertEqual('Remove consecutive semicolons.', oRule._get_solution(6))

    def test_fix_rule_001(self):
        oRule = semicolon.rule_001()
        oRule.fix(self.oFile)

        self.assertEqual(self.oFile.lines[6].line, '  signal sig2 : std_logic;')
        self.assertEqual(self.oFile.lines[7].line, '  signal sig3 : std_logic;')
        self.assertEqual(self.oFile.lines[9].line, '  signal sig4 : std_logic;signal sig5 : std_logic;')
        self.assertEqual(self.oFile.lines[11].line, '  signal sig6 : std_logic;signal sig7 : std_logic;signal sig8 : std_logic;')
        self.assertEqual(self.oFile.lines[13].line, '  signal sig9 : std_logic;signal sig10 : std_logic;signal sig11 : std_logic;')
        self.assertEqual(self.oFile.lines[15].line, '  signal sig12 : std_logic;signal sig13 : std_logic;signal sig14 : std_logic;')
        self.assertEqual(self.oFile.lines[18].line, '  signal sig15 : std_logic;signal sig16 : std_logic;signal sig17 : std_logic; --;;;')
        self.assertEqual(self.oFile.lines[21].line, '  signal sig18 : std_logic;signal sig19 : std_logic;signal sig20 : std_logic; --;;;')

        oRule.analyze(self.oFile)
        lExpected = []
        self.assertEqual(oRule.violations, lExpected)
       

