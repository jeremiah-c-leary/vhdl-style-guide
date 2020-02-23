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

        dExpected = [{'lineNumber': 15, 'label': 'LABEL2'},
                     {'lineNumber': 16, 'label': 'LABEL1'},

                     {'lineNumber': 22, 'label': 'LABEL2A1'},
                     {'lineNumber': 25, 'label': 'LABEL2A2A'},
                     {'lineNumber': 26, 'label': 'LABEL2A2'},
                     {'lineNumber': 28, 'label': 'LABEL2A3'},
                     {'lineNumber': 29, 'label': 'LABEL2A'},

                     {'lineNumber': 32, 'label': 'LABEL2B1'},
                     {'lineNumber': 34, 'label': 'LABEL2B2'},
                     {'lineNumber': 37, 'label': 'LABEL2B3A'},
                     {'lineNumber': 38, 'label': 'LABEL2B3'},
                     {'lineNumber': 39, 'label': 'LABEL2B'},

                     {'lineNumber': 43, 'label': 'LABEL2C1A'},
                     {'lineNumber': 44, 'label': 'LABEL2C1'},
                     {'lineNumber': 46, 'label': 'LABEL2C2'},
                     {'lineNumber': 48, 'label': 'LABEL2C3'},
                     {'lineNumber': 49, 'label': 'LABEL2C'},

                     {'lineNumber': 52, 'label': 'LABEL2D1'},
                     {'lineNumber': 54, 'label': 'LABEL2D2'},
                     {'lineNumber': 56, 'label': 'LABEL2D3'},
                     {'lineNumber': 57, 'label': 'LABEL2D'},

                     {'lineNumber': 58, 'label': 'LABEL1'},

                     {'lineNumber': 65, 'label': 'LABEL2'},
                     {'lineNumber': 66, 'label': 'LABEL1'}]

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

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
