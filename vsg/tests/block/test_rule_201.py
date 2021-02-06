
import os
import unittest

from vsg.rules import block
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_201_test_input.vhd'))

lExpected_require_blank_line = []
lExpected_require_blank_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_201_test_input.fixed_require_blank_line.vhd'), lExpected_require_blank_line, False)

lExpected_no_blank_line = []
lExpected_no_blank_line.append('')
utils.read_file(os.path.join(sTestDir, 'rule_201_test_input.fixed_no_blank_line.vhd'), lExpected_no_blank_line, False)


class test_block_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_201_require_blank_line(self):
        oRule = block.rule_201()
        oRule.style = 'require_blank_line'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block')
        self.assertEqual(oRule.identifier, '201')

        lExpected = [55, 60, 64]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_201_require_blank_line(self):
        oRule = block.rule_201()
        oRule.style = 'require_blank_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_201_no_blank_line(self):
        oRule = block.rule_201()
        oRule.style = 'no_blank_line'

        lExpected = [12, 23, 34, 49]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_201_no_blank_line(self):
        oRule = block.rule_201()
        oRule.style = 'no_blank_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_blank_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
