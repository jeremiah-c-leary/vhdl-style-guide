
import os
import unittest

from vsg.rules import block_comment
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_002_test_input.vhd'))


class test_block_comment_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_002_default(self):
        oRule = block_comment.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block_comment')
        self.assertEqual(oRule.identifier, '002')

        lExpected = []

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_plus(self):
        oRule = block_comment.rule_002()
        oRule.comment_left = '+'

        lExpected = [3, 4, 5, 15, 16, 17, 18, 22, 23, 24, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_bar(self):
        oRule = block_comment.rule_002()
        oRule.comment_left = '|'

        lExpected = [3, 4, 5, 9, 10, 11, 22, 23, 24, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_exclamation_dash_dash(self):
        oRule = block_comment.rule_002()
        oRule.comment_left = '!'

        lExpected = [3, 4, 5, 9, 10, 11, 15, 16, 17, 18]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

