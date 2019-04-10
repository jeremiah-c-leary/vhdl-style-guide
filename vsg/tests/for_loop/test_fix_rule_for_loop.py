import os

import unittest

from vsg.rules import for_loop
from vsg import vhdlFile
from vsg.tests import utils


class testFixRuleForLoopMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','for_loop','for_loop_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = for_loop.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[19].line, '      for index in 3 to 72 loop')
        self.assertEqual(self.oFile.lines[21].line, '        for j in 0 to 32 loop')
        self.assertEqual(self.oFile.lines[26].line, '      for index in 2 to 16 loop')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = for_loop.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[23].line, '        end loop;')
        self.assertEqual(self.oFile.lines[24].line, '      end loop;')
        self.assertEqual(self.oFile.lines[28].line, '      end loop;')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = for_loop.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[36].line, '    LABEL : for index in 10 to 200 loop')
        self.assertEqual(self.oFile.lines[40].line, '    LABEL: for index in 10 to 200 loop')
        self.assertEqual(self.oFile.lines[44].line, '    LABEL :for index in 10 to 200 loop')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = for_loop.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[40].line, '    Label : for index in 10 to 200 loop')
        self.assertEqual(self.oFile.lines[48].line, '    LABEL : for index in 10 to 200 loop')
        self.assertEqual(self.oFile.lines[52].line, '    LABEL :    for index in 10 to 200 loop')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = for_loop.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[44].line, '    LABEL : for index in 10 to 200 loop')
        self.assertEqual(self.oFile.lines[48].line, '    LABEL   : for index in 10 to 200 loop')
        self.assertEqual(self.oFile.lines[52].line, '    LABEL : for index in 10 to 200 loop')
        self.assertEqual(oRule.violations, dExpected)
