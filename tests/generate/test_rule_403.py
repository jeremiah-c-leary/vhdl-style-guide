# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import generate

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_403_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_403_test_input.fixed.vhd"), lExpected)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_403(self):
        oRule = generate.rule_403()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "403")

        lExpected = []
        lExpected.extend(range(42, 47))
        lExpected.extend(range(52, 57))
        lExpected.extend(range(62, 67))
        lExpected.extend(range(95, 97))
        lExpected.extend(range(103, 105))
        lExpected.extend(range(111, 113))
        lExpected.extend(range(125, 127))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_403(self):
        oRule = generate.rule_403()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
