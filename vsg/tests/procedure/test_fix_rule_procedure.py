import os

import unittest

from vsg.rules import procedure
from vsg import vhdlFile
from vsg.tests import utils



class testFixRuleProcedureMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'procedure_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = procedure.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[14].line, '  procedure AVERAGE_SAMPLES;')
        self.assertEqual(self.oFile.lines[16].line, '  procedure AVERAGE_SAMPLES (')

    def test_fix_rule_005(self):
        oRule = procedure.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[89].line, '    variable var_1 : integer;')
        self.assertEqual(self.oFile.lines[90].line, '    variable var_2 : integer;')

    def test_fix_rule_006(self):
        oRule = procedure.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[123].line, '    ) is')


    def test_fix_rule_008(self):
        oRule = procedure.rule_008()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = procedure.rule_009()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
