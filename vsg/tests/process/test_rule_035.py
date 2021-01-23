
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_035_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_035_test_input.fixed.vhd'), lExpected)

lExpectedCompactAlignmentFalse = []
lExpectedCompactAlignmentFalse.append('')
utils.read_file(os.path.join(sTestDir, 'rule_035_test_input.fixed_compact_alignment_false.vhd'), lExpectedCompactAlignmentFalse)


class test_process_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_035(self):
        oRule = process.rule_035()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '035')

        lExpected = [30, 31, 35, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_035(self):
        oRule = process.rule_035()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_035_compact_alignment_false(self):
        oRule = process.rule_035()
        oRule.compact_alignment = False
        oRule.include_lines_without_comments = False

        lExpected = [30, 31, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_035_compact_alignment_false(self):
        oRule = process.rule_035()
        oRule.compact_alignment = False
        oRule.include_lines_without_comments = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpectedCompactAlignmentFalse, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
