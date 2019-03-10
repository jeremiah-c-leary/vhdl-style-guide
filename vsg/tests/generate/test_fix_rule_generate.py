import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

class testFixRuleGenerateMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generate','generate_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(self.lFile)

    def test_fix_rule_001(self):
        oRule = generate.rule_001()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = generate.rule_002()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = generate.rule_003()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = generate.rule_004()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = generate.rule_005()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = generate.rule_008()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[29].line, '  end generate GENERATE_1;')

    def test_fix_rule_009(self):
        oRule = generate.rule_009()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[19].line, 'end GENERATE generate_1;')

    def test_fix_rule_010(self):
        oRule = generate.rule_010()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[19].line, 'END generate generate_1;')
        self.assertEqual(self.oFile.lines[62].line, '  end generate GENERATE_1;')

    def test_fix_rule_012(self):
        oRule = generate.rule_012()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[14].line, '   end generate GENERATE_1;')
        self.assertEqual(self.oFile.lines[19].line, 'END GENERATE GENERATE_1;')
        self.assertEqual(self.oFile.lines[73].line, '      end generate GENERATE_3;')

    def test_fix_rule_013(self):
        oRule = generate.rule_013()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[34].line, '  end generate GENERATE_1;')

    def test_fix_rule_014(self):
        oRule = generate.rule_014()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[21].line, '  GENERATE_1: if CONDITION = \'1\' generate')
        self.assertEqual(self.oFile.lines[26].line, '  GENERATE_1  : if  CONDITION = \'1\'  generate')
