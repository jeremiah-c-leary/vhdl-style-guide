import os
import unittest

from vsg.rules import ranges
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'range_test_input.vhd'))

class testFixRuleRange(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001_with_lowercase(self):
        oRule = ranges.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[17].line, '    G_GENERIC1 : std_logic_vector(3 downto 0);')
        self.assertEqual(self.oFile.lines[21].line, '    P_PORT1 : std_logic_vector(15 downto 6);')
        self.assertEqual(self.oFile.lines[28].line, '  constant c_const1 : std_logic_vector(3 downto 0);  -- downto')
        self.assertEqual(self.oFile.lines[33].line, '  signal w_sig1 : std_logic_vector(50 downto 45);')

        self.assertEqual('Change downto keyword to lowercase.', oRule._get_solution(0))

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001_with_uppercase(self):
        oRule = ranges.rule_001()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[5].line, '    G_GENERIC1 : std_logic_vector(3 DOWNTO 0);')
        self.assertEqual(self.oFile.lines[9].line, '    P_PORT1 : std_logic_vector(15 DOWNTO 6); -- DOWNTO')
        self.assertEqual(self.oFile.lines[17].line, '    G_GENERIC1 : std_logic_vector(3 DOWNTO 0);')
        self.assertEqual(self.oFile.lines[21].line, '    P_PORT1 : std_logic_vector(15 DOWNTO 6);')
        self.assertEqual(self.oFile.lines[29].line, '  constant c_const2 : std_logic_vector(3 DOWNTO 0);')
        self.assertEqual(self.oFile.lines[33].line, '  signal w_sig1 : std_logic_vector(50 DOWNTO 45);')
        self.assertEqual(self.oFile.lines[34].line, '  signal w_sig2 : std_logic_vector(50 DOWNTO 45);')

        self.assertEqual('Change downto keyword to uppercase.', oRule._get_solution(0))

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_with_lowercase(self):
        oRule = ranges.rule_002()
        oRule.case = 'lower'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[18].line, '    G_GENERIC2 : std_logic_vector(0 to 256)')
        self.assertEqual(self.oFile.lines[22].line, '    P_PORT2 : std_logic_vector(56 to 132)')
        self.assertEqual(self.oFile.lines[30].line, '  constant c_const3 : std_logic_vector(345 to 670);')
        self.assertEqual(self.oFile.lines[35].line, '  signal w_sig3 : std_logic_vector(46 to 345);')

        self.assertEqual('Change to keyword to lowercase.', oRule._get_solution(0))

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)


    def test_rule_002_with_uppercase(self):
        oRule = ranges.rule_002()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[6].line, '    G_GENERIC2 : std_logic_vector(0 TO 256)')
        self.assertEqual(self.oFile.lines[10].line, '    P_PORT2 : std_logic_vector(56 TO 132)')
        self.assertEqual(self.oFile.lines[22].line, '    P_PORT2 : std_logic_vector(56 TO 132)')
        self.assertEqual(self.oFile.lines[30].line, '  constant c_const3 : std_logic_vector(345 TO 670);')
        self.assertEqual(self.oFile.lines[31].line, '  constant c_const4 : std_logic_vector(345 TO 670);')
        self.assertEqual(self.oFile.lines[36].line, '  signal w_sig4 : std_logic_vector(46 TO 345);')

        self.assertEqual('Change to keyword to uppercase.', oRule._get_solution(0))

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
