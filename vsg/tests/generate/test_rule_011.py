import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'nested_generates_test_input.vhd'))

class testRuleGenerateMethods(unittest.TestCase):

    def setUp(self):
       self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_011(self):
        oRule = generate.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '011')

        lExpected = []

        dViolation = utils.add_violation(15)
        dViolation['label'] = 'LABEL2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['label'] = 'LABEL1'
        lExpected.append(dViolation)


        dViolation = utils.add_violation(22)
        dViolation['label'] = 'LABEL2A1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(25)
        dViolation['label'] = 'LABEL2A2A'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(26)
        dViolation['label'] = 'LABEL2A2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['label'] = 'LABEL2A3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(29)
        dViolation['label'] = 'LABEL2A'
        lExpected.append(dViolation)


        dViolation = utils.add_violation(32)
        dViolation['label'] = 'LABEL2B1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(34)
        dViolation['label'] = 'LABEL2B2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(37)
        dViolation['label'] = 'LABEL2B3A'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(38)
        dViolation['label'] = 'LABEL2B3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(39)
        dViolation['label'] = 'LABEL2B'
        lExpected.append(dViolation)


        dViolation = utils.add_violation(43)
        dViolation['label'] = 'LABEL2C1A'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(44)
        dViolation['label'] = 'LABEL2C1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(46)
        dViolation['label'] = 'LABEL2C2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(48)
        dViolation['label'] = 'LABEL2C3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(49)
        dViolation['label'] = 'LABEL2C'
        lExpected.append(dViolation)


        dViolation = utils.add_violation(52)
        dViolation['label'] = 'LABEL2D1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(54)
        dViolation['label'] = 'LABEL2D2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(56)
        dViolation['label'] = 'LABEL2D3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(57)
        dViolation['label'] = 'LABEL2D'
        lExpected.append(dViolation)


        dViolation = utils.add_violation(58)
        dViolation['label'] = 'LABEL1'
        lExpected.append(dViolation)


        dViolation = utils.add_violation(65)
        dViolation['label'] = 'LABEL2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(66)
        dViolation['label'] = 'LABEL1'
        lExpected.append(dViolation)


        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_011(self):
        oRule = generate.rule_011()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[15].line, '    end generate LABEL2;')
        self.assertTrue(self.oFile.lines[15].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[16].line, '  end generate LABEL1;')
        self.assertTrue(self.oFile.lines[16].isGenerateEndLabel)

        self.assertEqual(self.oFile.lines[22].line, '      end generate LABEL2A1;')
        self.assertTrue(self.oFile.lines[22].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[25].line, '        end generate LABEL2A2A;')
        self.assertTrue(self.oFile.lines[25].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[26].line, '      end generate LABEL2A2;')
        self.assertTrue(self.oFile.lines[26].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[28].line, '      end generate LABEL2A3;')
        self.assertTrue(self.oFile.lines[28].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[29].line, '    end generate LABEL2A;')
        self.assertTrue(self.oFile.lines[29].isGenerateEndLabel)

        self.assertEqual(self.oFile.lines[32].line, '      end generate LABEL2B1;')
        self.assertTrue(self.oFile.lines[32].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[34].line, '      end generate LABEL2B2;')
        self.assertTrue(self.oFile.lines[34].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[37].line, '        end generate LABEL2B3A;')
        self.assertTrue(self.oFile.lines[37].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[38].line, '      end generate LABEL2B3;')
        self.assertTrue(self.oFile.lines[38].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[39].line, '    end generate LABEL2B;')
        self.assertTrue(self.oFile.lines[39].isGenerateEndLabel)

        self.assertEqual(self.oFile.lines[43].line, '        end generate LABEL2C1A;')
        self.assertTrue(self.oFile.lines[43].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[44].line, '      end generate LABEL2C1;')
        self.assertTrue(self.oFile.lines[44].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[46].line, '      end generate LABEL2C2;')
        self.assertTrue(self.oFile.lines[46].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[48].line, '      end generate LABEL2C3;')
        self.assertTrue(self.oFile.lines[48].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[49].line, '    end generate LABEL2C;')
        self.assertTrue(self.oFile.lines[49].isGenerateEndLabel)

        self.assertEqual(self.oFile.lines[52].line, '      end generate LABEL2D1;')
        self.assertTrue(self.oFile.lines[52].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[54].line, '      end generate LABEL2D2;')
        self.assertTrue(self.oFile.lines[54].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[56].line, '      end generate LABEL2D3;')
        self.assertTrue(self.oFile.lines[56].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[57].line, '    end generate LABEL2D;')
        self.assertTrue(self.oFile.lines[57].isGenerateEndLabel)

        self.assertEqual(self.oFile.lines[58].line, '  end generate LABEL1;')
        self.assertTrue(self.oFile.lines[58].isGenerateEndLabel)

        self.assertEqual(self.oFile.lines[65].line, '    end generate LABEL2;')
        self.assertTrue(self.oFile.lines[65].isGenerateEndLabel)
        self.assertEqual(self.oFile.lines[66].line, '  end generate LABEL1;')
        self.assertTrue(self.oFile.lines[66].isGenerateEndLabel)

        self.assertEqual(oRule.violations, [])
