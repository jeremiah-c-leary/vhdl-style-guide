
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_026_test_input.vhd'))

lExpected_no_blank = []
lExpected_no_blank.append('')
utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_no_blank.vhd'), lExpected_no_blank)

lExpected_require_blank = []
lExpected_require_blank.append('')
utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_require_blank.vhd'), lExpected_require_blank)


class test_process_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_026_no_blank(self):
        oRule = process.rule_026()
        oRule.style = 'no_blank_line'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [7, 13, 19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_no_blank(self):
        self.maxDiff = None
        oRule = process.rule_026()
        oRule.style = 'no_blank_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_026_require_blank(self):
        oRule = process.rule_026()
        oRule.style = 'require_blank_line'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [27, 32, 37]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_require_blank(self):
        self.maxDiff = None
        oRule = process.rule_026()
        oRule.style = 'require_blank_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
