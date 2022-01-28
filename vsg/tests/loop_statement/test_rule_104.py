
import os
import unittest

from vsg.rules import loop_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_104_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_104_test_input.fixed.vhd'), lExpected)


class test_loop_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_104(self):
        oRule = loop_statement.rule_104()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'loop_statement')
        self.assertEqual(oRule.identifier, '104')

        lExpected = [17, 19, 31, 33, 45, 47]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_104(self):
        oRule = loop_statement.rule_104()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
