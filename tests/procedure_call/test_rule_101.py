# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import procedure_call

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_101_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_101_test_input.fixed.vhd"), lExpected, False)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_101(self):
        oRule = procedure_call.rule_101()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "101")

        lExpected = []
        lExpected.extend(range(38, 42))
        lExpected.extend(range(44, 48))
        lExpected.extend(range(53, 57))
        lExpected.extend(range(59, 63))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_101(self):
        oRule = procedure_call.rule_101()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
