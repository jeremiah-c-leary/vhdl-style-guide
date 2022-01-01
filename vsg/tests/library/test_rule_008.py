
import os
import unittest

from vsg.rules import library
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_008_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_008_test_input.fixed.vhd'), lExpected)

lExpected_with_indent_size_zero = []
lExpected_with_indent_size_zero.append('')
utils.read_file(os.path.join(sTestDir, 'rule_008_test_input.fixed_with_indent_size_0.vhd'), lExpected_with_indent_size_zero)


class test_library_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_008(self):
        oRule = library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '008')

        lExpected = [7, 8, 9]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_008(self):
        oRule = library.rule_008()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_indent_size_zero(self):
        oRule = library.rule_008()
        oRule.indentSize = 0

        lExpected = [3, 4, 8, 9]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_008_indent_size_zero(self):
        oRule = library.rule_008()
        oRule.indentSize = 0

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_with_indent_size_zero, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
