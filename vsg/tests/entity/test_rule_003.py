
import os
import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))

lExpected_require_blank = []
lExpected_require_blank.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_require_blank.vhd'), lExpected_require_blank)

lExpected_no_code = []
lExpected_no_code.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_no_code.vhd'), lExpected_no_code)

lExpected_allow_comment = []
lExpected_allow_comment.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_allow_comment.vhd'), lExpected_allow_comment)

lExpected_require_comment = []
lExpected_require_comment.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_require_comment.vhd'), lExpected_require_comment)


class test_entity_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_003_w_require_blank(self):
        oRule = entity.rule_003()
        oRule.style = 'require_blank_line'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [3, 8, 18, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_w_no_code(self):
        oRule = entity.rule_003()
        oRule.style = 'no_code'

        lExpected = [8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_w_allow_comment(self):
        oRule = entity.rule_003()
        oRule.style = 'allow_comment'

        lExpected = [8, 21]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_w_require_comment(self):
        oRule = entity.rule_003()
        oRule.style = 'require_comment'

        lExpected = [8, 21, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_w_require_blank(self):
        oRule = entity.rule_003()
        oRule.style = 'require_blank_line'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003_w_no_code(self):
        oRule = entity.rule_003()
        oRule.style = 'no_code'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_code, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003_w_allow_comment(self):
        oRule = entity.rule_003()
        oRule.style = 'allow_comment'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_allow_comment, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003_w_require_comment(self):
        oRule = entity.rule_003()
        oRule.style = 'require_comment'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_comment, lActual)

        lExpected = [8, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

