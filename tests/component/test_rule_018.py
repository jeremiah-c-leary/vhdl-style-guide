
import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_018_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_require_blank_line(self):
        oRule = component.rule_018()
        oRule.style = 'require_blank_line'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '018')

        lExpected = [12, 19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_require_blank_line(self):
        oRule = component.rule_018()
        oRule.style = 'require_blank_line'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_018_test_input.fixed.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_require_blank_line_unless_pragma(self):
        oRule = component.rule_018()
        oRule.style = 'require_blank_line_unless_pragma'

        lExpected = [12]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_require_blank_line_unless_pragma(self):
        oRule = component.rule_018()
        oRule.style = 'require_blank_line_unless_pragma'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_018_test_input.fixed_pragma.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
