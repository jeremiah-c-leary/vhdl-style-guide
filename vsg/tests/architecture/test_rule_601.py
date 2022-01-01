
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_601_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_601_test_input.fixed.vhd'), lExpected)


class test_architecture_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_601(self):
        oRule = architecture.rule_601()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '601')
        self.assertEqual(oRule.groups, ['case'])

        lExpected = []
        lExpected.extend([146, 147, 148, 154, 154, 154, 157, 158, 159, 163, 164, 165, 169, 170, 171, 178, 179, 180, 188, 189, 190])
        lExpected.extend([341, 342, 343, 349, 349, 349, 352, 353, 354, 358, 359, 360, 364, 365, 366, 373, 374, 375, 383, 384, 385]) 

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_601(self):
        oRule = architecture.rule_601()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
