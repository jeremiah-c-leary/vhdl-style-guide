
import os
import unittest

from vsg.rules import file_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed.vhd'), lExpected)


class test_file_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = file_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '001')

        lExpected = [15, 17, 18, 20, 21, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001(self):
        oRule = file_statement.rule_001()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
