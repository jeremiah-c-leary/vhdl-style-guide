# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import package_instantiation

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_100_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_100_test_input.fixed.vhd"), lExpected)


class test_package_instantiation_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_100(self):
        oRule = package_instantiation.rule_100()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "package_instantiation")
        self.assertEqual(oRule.identifier, "100")

        lExpected = [7]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_100(self):
        oRule = package_instantiation.rule_100()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
