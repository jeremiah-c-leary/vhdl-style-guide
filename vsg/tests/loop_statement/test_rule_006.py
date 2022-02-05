
import os
import unittest

from vsg.rules import loop_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_006_test_input.vhd'))

dIndentMap = utils.read_indent_file()


class test_loop_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_006(self):
        oRule = loop_statement.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'loop_statement')
        self.assertEqual(oRule.identifier, '006')

        lExpected = [20, 22, 24, 31, 33, 35, 42, 44, 46]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
