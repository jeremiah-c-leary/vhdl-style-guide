# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import variable

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_400_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected__align_left_yes__align_paren_no = []
lExpected__align_left_yes__align_paren_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed__align_left_yes__align_paren_no.vhd"), lExpected__align_left_yes__align_paren_no)

lExpected__align_left_yes__align_paren_yes = []
lExpected__align_left_yes__align_paren_yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed__align_left_yes__align_paren_yes.vhd"), lExpected__align_left_yes__align_paren_yes)

lExpected__align_left_no__align_paren_yes = []
lExpected__align_left_no__align_paren_yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed__align_left_no__align_paren_yes.vhd"), lExpected__align_left_no__align_paren_yes)

lExpected__align_left_no__align_paren_no = []
lExpected__align_left_no__align_paren_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed__align_left_no__align_paren_no.vhd"), lExpected__align_left_no__align_paren_no)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)
        self.maxDiff = None

    def test_rule_400__align_left_yes__align_paren_no(self):
        oRule = variable.rule_400()
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.extend(range(5, 20))
        # lExpected.extend(range(22, 26))
        lExpected.extend(range(28, 32))
        lExpected.extend(range(34, 36))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400__align_left_yes__align_paren_no(self):
        oRule = variable.rule_400()
        oRule.align_left = "yes"
        oRule.align_paren = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_yes__align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_400__align_left_true__align_paren_false(self):
        oRule = variable.rule_400()
        oRule.align_left = True
        oRule.align_paren = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_yes__align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400__align_left_no__align_paren_no(self):
        oRule = variable.rule_400()
        oRule.align_left = "no"
        oRule.align_paren = "no"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.extend(range(4, 20))
        # lExpected.extend(range(22, 26))
        lExpected.extend(range(28, 32))
        lExpected.extend(range(34, 36))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400__align_left_no__align_paren_no(self):
        oRule = variable.rule_400()
        oRule.align_left = "no"
        oRule.align_paren = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_no__align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_400__align_left_false__align_paren_false(self):
        oRule = variable.rule_400()
        oRule.align_left = False
        oRule.align_paren = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_no__align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400__align_left_no__align_paren_yes(self):
        oRule = variable.rule_400()
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.extend(range(4, 20))
        # lExpected.extend(range(22, 26))
        lExpected.extend(range(28, 32))
        lExpected.extend(range(34, 36))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400__align_left_no__align_paren_yes(self):
        oRule = variable.rule_400()
        oRule.align_left = "no"
        oRule.align_paren = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_no__align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_400__align_left_false__align_paren_true(self):
        oRule = variable.rule_400()
        oRule.align_left = False
        oRule.align_paren = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_no__align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400__align_left_yes__align_paren_yes(self):
        oRule = variable.rule_400()
        oRule.align_left = "yes"
        oRule.align_paren = "yes"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.extend(range(5, 20))
        # lExpected.extend(range(22, 26))
        lExpected.extend(range(28, 32))
        lExpected.extend(range(34, 36))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400__align_left_yes__align_paren_yes(self):
        oRule = variable.rule_400()
        oRule.align_left = "yes"
        oRule.align_paren = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_yes__align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_400__align_left_true__align_paren_true(self):
        oRule = variable.rule_400()
        oRule.align_left = True
        oRule.align_paren = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected__align_left_yes__align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
