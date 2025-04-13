# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import instantiation

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_034_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_034_w_default(self):
        oRule = instantiation.rule_034()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "instantiation")
        self.assertEqual(oRule.identifier, "034")
        self.assertEqual(oRule.groups, ["structure"])

        lExpected = [30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_034_w_entity(self):
        oRule = instantiation.rule_034()
        oRule.method = "entity"

        lExpected = [6, 18]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
