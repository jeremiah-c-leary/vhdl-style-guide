import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests

lFileRule010 = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'architecture_test_input.vhd'))
oFileRule010 = vhdlFile.vhdlFile(lFileRule010)

lFileIs = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'architecture_is_test_input.vhd'))
oFileIs = vhdlFile.vhdlFile(lFileIs)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'architecture_test_input.vhd'))

class testFixRuleArchitectureMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = architecture.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = architecture.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = architecture.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004_lowercase(self):
        oRule = architecture.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[20].line, ' architecture ARch Of entity Is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004_uppercase(self):
        oRule = architecture.rule_004()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[20].line, ' ARCHITECTURE ARch Of entity Is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = architecture.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = architecture.rule_008()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = architecture.rule_009()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = architecture.rule_010()
        dExpected = []
        oRule.fix(oFileRule010)
        oRule.analyze(oFileRule010)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = architecture.rule_012()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014_uppercase(self):
        oRule = architecture.rule_014()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[81].line, 'architecture ARCH of ENT is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014_lowercase(self):
        oRule = architecture.rule_014()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[59].line, 'architecture ARCH of entity is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015(self):
        oRule = architecture.rule_015()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_016(self):
        oRule = architecture.rule_016()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_017(self):
        oRule = architecture.rule_017()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_018(self):
        oRule = architecture.rule_018()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_019_lowercase(self):
        oRule = architecture.rule_019()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[20].line, ' Architecture ARch of entity Is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_019_uppercase(self):
        oRule = architecture.rule_019()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[20].line, ' Architecture ARch OF entity Is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_020_lowercase(self):
        oRule = architecture.rule_020()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[20].line, ' Architecture ARch Of entity is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_020_uppercase(self):
        oRule = architecture.rule_020()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[20].line, ' Architecture ARch Of entity IS')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_021_lowercase(self):
        oRule = architecture.rule_021()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[29].line, 'begin')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_021_uppercase(self):
        oRule = architecture.rule_021()
        oRule.case = 'upper'
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[39].line, 'BEGIN')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_022(self):
        oRule = architecture.rule_022()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_024(self):
        oRule = architecture.rule_024()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[13].line, 'end Architecture ARCH;')
        self.assertEqual(self.oFile.lines[77].line, 'end ARCH;')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_027(self):
        oRule = architecture.rule_027()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

