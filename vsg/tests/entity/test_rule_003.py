
import os
import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed.vhd'), lExpected)

lExpected_allow_comments = []
lExpected_allow_comments.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_allow_comments.vhd'), lExpected_allow_comments)

lExpected_allow_comments_and_blank_above_comment = []
lExpected_allow_comments_and_blank_above_comment.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_allow_comments_and_blank_above_comment.vhd'), lExpected_allow_comments_and_blank_above_comment)


class test_entity_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_003_wo_allow_comments(self):
        oRule = entity.rule_003()
        oRule.allow_comments = False
        oRule.blank_above_comment = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [3, 8, 18, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_w_allow_comments(self):
        oRule = entity.rule_003()
        oRule.allow_comments = True
        oRule.blank_above_comment = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_w_allow_comments_and_blank_above_comment(self):
        oRule = entity.rule_003()
        oRule.allow_comments = True
        oRule.blank_above_comment = True

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [8, 21]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003(self):
        oRule = entity.rule_003()
        oRule.allow_comments = False
        oRule.blank_above_comment = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003_w_allow_comments(self):
        oRule = entity.rule_003()
        oRule.allow_comments = True
        oRule.blank_above_comment = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_allow_comments, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003_w_allow_comments_and_blank_above_comment(self):
        oRule = entity.rule_003()
        oRule.allow_comments = True
        oRule.blank_above_comment = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_allow_comments_and_blank_above_comment, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

