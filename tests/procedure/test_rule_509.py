# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import procedure

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_509_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_509_test_input.fixed.vhd"), lExpected)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)
        self.maxDiff = None

    def test_rule_509(self):
        oRule = procedure.rule_509()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "509")
        self.assertEqual(oRule.groups, ["case", "case::name"])

        lExpected = []
        lExpected.extend([13, 14, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 25, 26, 27, 27, 28, 29, 30, 75, 78, 155])
        lExpected.extend([158, 158, 169, 175, 176, 177, 178, 180, 184, 188, 195, 195, 196, 196, 197, 197, 198, 198])
        lExpected.extend([199, 199, 200, 201, 202, 203, 203, 204, 205, 206, 209, 210, 211, 212, 213])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_509(self):
        oRule = procedure.rule_509()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
