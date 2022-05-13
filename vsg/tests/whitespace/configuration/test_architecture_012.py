
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


class test(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_max_1_min_1(self):
        oRule = architecture.rule_012()
        oRule.maximum_number_of_spaces = 1
        oRule.minimum_number_of_spaces = 1

        lExpected = [17, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_max_1_min_1(self):
        self.maxDiff = None
        oRule = architecture.rule_012()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_min_1_max_1, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_max_2_min_2(self):
        oRule = architecture.rule_012()
        oRule.maximum_number_of_spaces = 2
        oRule.minimum_number_of_spaces = 2

        lExpected = [8, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_max_2_min_2(self):
        oRule = architecture.rule_012()
        oRule.maximum_number_of_spaces = 2
        oRule.minimum_number_of_spaces = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_min_2_max_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

