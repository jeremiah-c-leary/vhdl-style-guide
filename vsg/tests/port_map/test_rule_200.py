
import os
import unittest

from vsg.rules import port_map
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_200_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_200_test_input.fixed.vhd'), lExpected)


class test_port_map_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_200(self):
        oRule = port_map.rule_200()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port_map')
        self.assertEqual(oRule.identifier, '200')
        self.assertEqual(oRule.groups, ['blank_line'])

        lExpected = [27, 40]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_200(self):
        oRule = port_map.rule_200()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
