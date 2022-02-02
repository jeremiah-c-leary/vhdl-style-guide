
import os
import unittest

from vsg.rules import package
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_019_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_019_test_input.fixed.vhd'), lExpected)


class test_package_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_019(self):
        oRule = package.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package')
        self.assertEqual(oRule.identifier, '019')

        lExpected = []
        lExpected.extend([6, 8, 9, 10, 11])
        lExpected.extend([23, 25, 26, 28, 29])
        lExpected.extend([47])
        lExpected.extend([85, 87, 88, 89])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_019(self):
        oRule = package.rule_019()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
