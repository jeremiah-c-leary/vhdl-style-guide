import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentConstantName(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_013(self):
        oRule = constant.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [5, 12, 17, 20]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = constant.rule_013()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[5].line, '  constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => \'1\');')
        self.assertEqual(self.oFile.lines[12].line, '  data <= c_ones;')
        self.assertEqual(self.oFile.lines[17].line, '    data <= c_ones;')
        self.assertEqual(self.oFile.lines[20].line, '      data <= c_zeros;')
        self.assertEqual(self.oFile.lines[28].line, '      data <= c_zeros;')

        self.assertEqual(oRule.violations, [])
