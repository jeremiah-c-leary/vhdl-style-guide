
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_026_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_allowing_comments_and_blank_lines.vhd'), lExpected)


class test_architecture_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_026_allowing_comments_and_blank_lines(self):
        oRule = architecture.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_allowing_comments_and_blank_lines(self):
        oRule = architecture.rule_026()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
