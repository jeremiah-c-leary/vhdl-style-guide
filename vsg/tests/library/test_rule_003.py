
import os
import unittest

from vsg.rules import library
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))

lExpected_default = []
lExpected_default.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_default.vhd'), lExpected_default)

lExpected_allow_library_clause = []
lExpected_allow_library_clause.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_allow_library_clause.vhd'), lExpected_allow_library_clause)


class test_library_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_003(self):
        oRule = library.rule_003()
        oRule.style = 'no_code'
        oRule.allow_library_clause = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [3, 6, 7]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003(self):
        oRule = library.rule_003()
        oRule.style = 'no_code'
        oRule.allow_library_clause = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_default, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_w_allow_library_clause(self):
        oRule = library.rule_003()
        oRule.allow_library_clause = True

        lExpected = [5]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_w_allow_library_clause(self):
        oRule = library.rule_003()
        oRule.allow_library_clause = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_allow_library_clause, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
