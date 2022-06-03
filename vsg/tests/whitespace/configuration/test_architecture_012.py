
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'configuration_test_input.vhd'))

lExpected_min_1_max_1 = []
lExpected_min_1_max_1.append('')
utils.read_file(os.path.join(sTestDir, 'architecture_012', 'configuration_test_input.fixed_min_1_max_1.vhd'), lExpected_min_1_max_1)

lExpected_min_2_max_2 = []
lExpected_min_2_max_2.append('')
utils.read_file(os.path.join(sTestDir, 'architecture_012', 'configuration_test_input.fixed_min_2_max_2.vhd'), lExpected_min_2_max_2)

lExpected_min_2_max_5 = []
lExpected_min_2_max_5.append('')
utils.read_file(os.path.join(sTestDir, 'architecture_012', 'configuration_test_input.fixed_min_2_max_5.vhd'), lExpected_min_2_max_5)

lExpected_min_2_max_10 = []
lExpected_min_2_max_10.append('')
utils.read_file(os.path.join(sTestDir, 'architecture_012', 'configuration_test_input.fixed_min_2_max_10.vhd'), lExpected_min_2_max_10)

lExpected_spaces_gte2 = []
lExpected_spaces_gte2.append('')
utils.read_file(os.path.join(sTestDir, 'architecture_012', 'configuration_test_input.fixed_spaces_gte2.vhd'), lExpected_spaces_gte2)

lExpected_spaces_gt2 = []
lExpected_spaces_gt2.append('')
utils.read_file(os.path.join(sTestDir, 'architecture_012', 'configuration_test_input.fixed_spaces_gt2.vhd'), lExpected_spaces_gt2)


class test(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_spaces_1(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = 1

        lExpected = [17, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_spaces_1(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_min_1_max_1, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_spaces_2(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = 2

        lExpected = [8, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_spaces_2(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_min_2_max_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_spaces_gte2(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = '>=2'

        lExpected = [8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_spaces_gte2(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = '>=2'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces_gte2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_spaces_gt2(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = '>2'

        lExpected = [8, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_spaces_gt2(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = '>2'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces_gt2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_spaces_2_plus(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = '2+'

        lExpected = [8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_spaces_2_plus(self):
        oRule = architecture.rule_012()
        oRule.number_of_spaces = '2+'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces_gte2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

