
import os
import unittest

from vsg.rules import port_map
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_004_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_004_test_input.fixed.vhd'), lExpected, True)

lExpected_same_line = []
lExpected_same_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_004_test_input.fixed_same_line.vhd'), lExpected_same_line, True)


class test_port_map_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_004(self):
        oRule = port_map.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port_map')
        self.assertEqual(oRule.identifier, '004')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_004(self):
        oRule = port_map.rule_004()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_004_same_line(self):
        oRule = port_map.rule_004()
        oRule.action = 'same_line'

        lExpected = [15, 28, 33, 38, 43, 48, 53, 58, 63]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_004_same_line(self):
        oRule = port_map.rule_004()
        oRule.action = 'same_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_same_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

