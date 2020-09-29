
import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_019_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_019_test_input.fixed.vhd'), lExpected)


class test_component_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    @unittest.skip('Saving this for later when I figure out how to deal with it.')
    def test_rule_019(self):
        oRule = component.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '019')

        lExpected = [6, 7, 8, 11, 12, 13, 20, 22, 25, 26, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Saving this for later when I figure out how to deal with it.')
    def test_fix_rule_019(self):
        oRule = component.rule_019()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
