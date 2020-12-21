
import os
import unittest

from vsg.rules import while_loop
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_002_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_002_test_input.fixed.vhd'), lExpected)


class test_while_loop_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_002(self):
        oRule = while_loop.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'while_loop')
        self.assertEqual(oRule.identifier, '002')

        lExpected = [15, 19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002(self):
        oRule = while_loop.rule_002()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
