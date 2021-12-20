
import os
import unittest

from vsg import parser
from vsg.rules import comment
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_011_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_011_test_input.fixed.vhd'), lExpected)


class test_comment_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_011(self):
        oRule = comment.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'comment')
        self.assertEqual(oRule.identifier, '011')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [5, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011(self):
        oRule = comment.rule_011()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

        oAllTokens = self.oFile.get_all_tokens()
        for oToken in oAllTokens.lTokens:
            if isinstance(oToken, parser.comment):
#                print(f'{oToken} | {oToken.indent}')
                self.assertIsNotNone(oToken.indent)

