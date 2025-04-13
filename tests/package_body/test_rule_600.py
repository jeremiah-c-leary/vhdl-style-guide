# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import package_body

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_600_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_600(self):
        oRule = package_body.rule_600()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "package_body")
        self.assertEqual(oRule.identifier, "600")

        lExpected = [6, 8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_600_capitalized(self):
        oRule = package_body.rule_600()
        oRule.suffixes = ["_PKG"]
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "package_body")
        self.assertEqual(oRule.identifier, "600")

        lExpected = [6, 8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
