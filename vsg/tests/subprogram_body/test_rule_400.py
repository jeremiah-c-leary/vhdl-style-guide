
import os
import unittest

from vsg.rules import subprogram_body
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_400_test_input.vhd'))

lExpected_all = []
lExpected_all.append('')
utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed.vhd'), lExpected_all)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400(self):
        oRule = subprogram_body.rule_400()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subprogram_body')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [8, 10, 15, 16, 17, 25, 27, 39, 41, 60, 62, 69]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400(self):
        oRule = subprogram_body.rule_400()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
