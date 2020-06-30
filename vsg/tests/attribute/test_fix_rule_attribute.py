import os

import unittest

from vsg.rules import attribute
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'attribute_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testFixRuleAttributeMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = attribute.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[9].line, '  ATTRIBUTE ram_init_file : string;')
        self.assertEqual(oFile.lines[11].line, '  attribute      ram_init_file of ram_block :')
        self.assertEqual(oFile.lines[12].line, '    signal is "contents.mif";')

    def test_fix_rule_002(self):
        oRule = attribute.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[9].line, '  attribute ram_init_file : string;')
