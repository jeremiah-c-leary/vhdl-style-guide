
import os
import unittest

from vsg.rules import library
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))


class test_library_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_007_no_blank_line(self):
        oRule = library.rule_007()
        oRule.style = 'no_blank_line'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '007')

        lExpected = [11, 16, 22, 24, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007_no_blank_line(self):
        oRule = library.rule_007()
        oRule.style = 'no_blank_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_no_blank_line.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_no_blank_line_unless_different_library(self):
        oRule = library.rule_007()
        oRule.style = 'no_blank_line_unless_different_library'

        lExpected = [11, 16, 22, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007_no_blank_line_unless_different_library(self):
        oRule = library.rule_007()
        oRule.style = 'no_blank_line_unless_different_library'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_no_blank_line_unless_different_library.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
