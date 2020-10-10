
import os
import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_021_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_021_test_input.fixed.vhd'), lExpected)


class test_instantiation_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_021(self):
        oRule = instantiation.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '021')

        lExpected = [26, 26, 36]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_021(self):
        oRule = instantiation.rule_021()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
