# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import library

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_012_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012(self):
        oRule = library.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "library")
        self.assertEqual(oRule.identifier, "012")
        self.assertFalse(oRule.fixable)
        self.assertTrue(oRule.disable)
        self.assertEqual(oRule.groups, ["naming"])

        lExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: ", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = []
        oRule.names.append("ieee")
        lExpected = [2]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: ieee", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["work"]
        lExpected = [3]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: work", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["std"]
        lExpected = [4]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: std", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["bad_lib"]
        lExpected = [5]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: bad_lib", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["ieee", "bad_lib"]
        lExpected = [2, 5]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: ieee, bad_lib", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["ieee", "work", "std"]
        lExpected = [2, 3, 4]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: ieee, work, std", oRule._get_solution(None))

        oRule.violations = []
        oRule.names = ["ieee", "work", "std", "bad_lib"]
        lExpected = [2, 3, 4, 5]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual("Library name is on list of restricted names: ieee, work, std, bad_lib", oRule._get_solution(None))
