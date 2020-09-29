
import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed.vhd'), lExpected)


class test_component_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_003(self):
        oRule = component.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003(self):
        oRule = component.rule_003()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
