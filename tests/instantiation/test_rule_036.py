# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import instantiation

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_036_test_input.vhd"))


class test_instantiation_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_036_add(self):
        oRule = instantiation.rule_036()
        oRule.action = "add"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "instantiation")
        self.assertEqual(oRule.identifier, "036")
        self.assertEqual(oRule.groups, ["structure", "structure::optional"])

        lExpected = [30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_036_remove(self):
        oRule = instantiation.rule_036()
        oRule.action = "remove"

        lExpected = [42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
