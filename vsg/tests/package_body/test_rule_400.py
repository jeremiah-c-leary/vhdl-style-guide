
import os
import unittest

from vsg.rules import package_body
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_400_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed.vhd'), lExpected)


class test_package_body_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400(self):
        oRule = package_body.rule_400()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package_body')
        self.assertEqual(oRule.identifier, '400')

        lExpected = []
        lExpected.extend([7, 8, 9])
        lExpected.extend([19, 20, 21, 23])
        lExpected.extend([27, 28])
        lExpected.append(41)
        lExpected.extend([80, 81, 82])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400(self):
        oRule = package_body.rule_400()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
