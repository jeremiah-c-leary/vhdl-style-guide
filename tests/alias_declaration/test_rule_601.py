# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import alias_declaration

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_601_test_input.vhd"))


class test_alias_declaration_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_601(self):
        oRule = alias_declaration.rule_601()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "alias_declaration")
        self.assertEqual(oRule.identifier, "601")

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
