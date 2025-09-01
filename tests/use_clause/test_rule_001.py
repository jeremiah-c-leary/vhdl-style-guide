# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import use_clause

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_001_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_001(self):
        oRule = use_clause.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.names, ["std_logic_arith"])
        self.assertEqual(oRule.name, "use_clause")
        self.assertEqual(oRule.identifier, "001")
        self.assertFalse(oRule.fixable)
        self.assertFalse(oRule.disable)
        self.assertEqual(oRule.groups, ["naming"])

        lExpected = []
        oRule.names = []
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: ", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = []
        oRule.names.append("std_logic_arith")
        lExpected = [3]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: std_logic_arith", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["std_logic_1164"]
        lExpected = [4]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: std_logic_1164", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["env"]
        lExpected = [7]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: env", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["bad_pkg"]
        lExpected = [10]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: bad_pkg", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["std_logic_arith", "bad_pkg"]
        lExpected = [3, 10]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: std_logic_arith, bad_pkg", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["std_logic_arith", "std_logic_1164", "env"]
        lExpected = [3, 4, 7]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: std_logic_arith, std_logic_1164, env", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["std_logic_arith", "std_logic_1164", "env", "bad_pkg"]
        lExpected = [3, 4, 7, 10]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Package name is on list of restricted names: std_logic_arith, std_logic_1164, env, bad_pkg", oRule._get_solution(None))
