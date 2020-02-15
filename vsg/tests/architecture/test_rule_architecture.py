import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_comment_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(lFileComment)

lFileIs = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'architecture_is_test_input.vhd'))
oFileIs = vhdlFile.vhdlFile(lFileIs)

lFileEnd = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'architecture_end_test_input.vhd'))
oFileEnd = vhdlFile.vhdlFile(lFileEnd)

lFileName = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'architecture_name_test_input.vhd'))
oFileName = vhdlFile.vhdlFile(lFileName)

class testRuleArchitectureMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = architecture.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = architecture.rule_001()

        dExpected = [9,20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = architecture.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = architecture.rule_002()

        dExpected = [14]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = architecture.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = architecture.rule_003()

        dExpected = [14]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = architecture.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004_lowercase(self):
        oRule = architecture.rule_004()

        dExpected = [{'line_number': 20, 'words_to_fix': {'Architecture'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_uppercase(self):
        oRule = architecture.rule_004()
        oRule.case = 'upper'

        dExpected = [{'line_number': 3, 'words_to_fix': {'architecture'}},
                    {'line_number': 9, 'words_to_fix': {'architecture'}},
                    {'line_number': 14, 'words_to_fix': {'architecture'}},
                    {'line_number': 20, 'words_to_fix': {'Architecture'}},
                    {'line_number': 26, 'words_to_fix': {'architecture'}},
                    {'line_number': 33, 'words_to_fix': {'architecture'}},
                    {'line_number': 37, 'words_to_fix': {'architecture'}},
                    {'line_number': 47, 'words_to_fix': {'architecture'}},
                    {'line_number': 59, 'words_to_fix': {'architecture'}},
                    {'line_number': 81, 'words_to_fix': {'architecture'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = architecture.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '005')

    def test_rule_005(self):
        oRule = architecture.rule_005()

        dExpected = [26]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = architecture.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = architecture.rule_006()

        dExpected = [2,9]
        oRule.analyze(oFileIs)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = architecture.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [22]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = architecture.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [24,31]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = architecture.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [{'line_number': 7, 'words_to_fix': {'End'}},
                     {'line_number': 13, 'words_to_fix': {'Architecture'}},
                     {'line_number': 24, 'words_to_fix': {'eND'}},
                     {'line_number': 31, 'words_to_fix': {'archITecture'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = architecture.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [55,77]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_architecture_end(self):
        oRule = architecture.rule_010()
        dExpected = []
        oRule.analyze(oFileEnd)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_uppercase(self):
        oRule = architecture.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [{'line_number': 24, 'words_to_fix': {'ArCh'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_lowercase(self):
        oRule = architecture.rule_011()
        oRule.case = 'lower'
        dExpected = [{'line_number': 7, 'words_to_fix': {'ARCH'}},
                     {'line_number': 18, 'words_to_fix': {'ARCH'}},
                     {'line_number': 24, 'words_to_fix': {'ArCh'}},
                     {'line_number': 31, 'words_to_fix': {'ARCH'}},
                     {'line_number': 35, 'words_to_fix': {'ARCH'}},
                     {'line_number': 45, 'words_to_fix': {'ARCH'}},
                     {'line_number': 55, 'words_to_fix': {'ARCH'}},
                     {'line_number': 85, 'words_to_fix': {'ARCH'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = architecture.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [7,18]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013_uppercase(self):
        oRule = architecture.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [{'line_number': 3, 'words_to_fix': {'Arch'}},
                     {'line_number': 20, 'words_to_fix': {'ARch'}},
                     {'line_number': 26, 'words_to_fix': {'ARch'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013_lowercase(self):
        oRule = architecture.rule_013()
        oRule.case = 'lower'
        dExpected = [{'line_number': 3, 'words_to_fix': {'Arch'}},
                     {'line_number': 9, 'words_to_fix': {'ARCH'}},
                     {'line_number': 14, 'words_to_fix': {'ARCH'}},
                     {'line_number': 20, 'words_to_fix': {'ARch'}},
                     {'line_number': 26, 'words_to_fix': {'ARch'}},
                     {'line_number': 33, 'words_to_fix': {'ARCH'}},
                     {'line_number': 37, 'words_to_fix': {'ARCH'}},
                     {'line_number': 47, 'words_to_fix': {'ARCH'}},
                     {'line_number': 59, 'words_to_fix': {'ARCH'}},
                     {'line_number': 81, 'words_to_fix': {'ARCH'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014_uppercase(self):
        oRule = architecture.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '014')
        dExpected = [{'line_number': 9, 'words_to_fix': {'EntITY'}},
                     {'line_number': 20, 'words_to_fix': {'entity'}},
                     {'line_number': 81, 'words_to_fix': {'ent'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014_lowercase(self):
        oRule = architecture.rule_014()
        oRule.case = 'lower'
        dExpected = [{'line_number': 3, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 9, 'words_to_fix': {'EntITY'}},
                     {'line_number': 14, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 33, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 37, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 47, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 59, 'words_to_fix': {'ENTITY'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = architecture.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [26,33]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = architecture.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '016')
        dExpected = [34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = architecture.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '017')
        dExpected = [34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = architecture.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '018')
        dExpected = [35]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019_lowercase(self):
        oRule = architecture.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '019')
        dExpected = [{'line_number': 20, 'words_to_fix': {'Of'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019_uppercase(self):
        oRule = architecture.rule_019()
        oRule.case = 'upper'
        dExpected = [{'line_number': 3, 'words_to_fix': {'of'}},
                     {'line_number': 9, 'words_to_fix': {'of'}},
                     {'line_number': 14, 'words_to_fix': {'of'}},
                     {'line_number': 20, 'words_to_fix': {'Of'}},
                     {'line_number': 33, 'words_to_fix': {'of'}},
                     {'line_number': 37, 'words_to_fix': {'of'}},
                     {'line_number': 47, 'words_to_fix': {'of'}},
                     {'line_number': 59, 'words_to_fix': {'of'}},
                     {'line_number': 81, 'words_to_fix': {'of'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_lowercase(self):
        oRule = architecture.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '020')
        dExpected = [{'line_number': 20, 'words_to_fix': {'Is'}},
                     {'line_number': 33, 'words_to_fix': {'iS'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_uppercase(self):
        oRule = architecture.rule_020()
        oRule.case = 'upper'
        dExpected = [{'line_number': 3, 'words_to_fix': {'is'}},
                     {'line_number': 9, 'words_to_fix': {'is'}},
                     {'line_number': 14, 'words_to_fix': {'is'}},
                     {'line_number': 20, 'words_to_fix': {'Is'}},
                     {'line_number': 33, 'words_to_fix': {'iS'}},
                     {'line_number': 37, 'words_to_fix': {'is'}},
                     {'line_number': 47, 'words_to_fix': {'is'}},
                     {'line_number': 59, 'words_to_fix': {'is'}},
                     {'line_number': 81, 'words_to_fix': {'is'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021_lowercase(self):
        oRule = architecture.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '021')
        dExpected = [{'line_number': 29, 'words_to_fix': {'BEGIN'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021_uppercase(self):
        oRule = architecture.rule_021()
        oRule.case = 'upper'
        dExpected = [{'line_number': 5, 'words_to_fix': {'begin'}},
                     {'line_number': 11, 'words_to_fix': {'begin'}},
                     {'line_number': 16, 'words_to_fix': {'begin'}},
                     {'line_number': 22, 'words_to_fix': {'begin'}},
                     {'line_number': 34, 'words_to_fix': {'begin'}},
                     {'line_number': 39, 'words_to_fix': {'begin'}},
                     {'line_number': 49, 'words_to_fix': {'begin'}},
                     {'line_number': 61, 'words_to_fix': {'begin'}},
                     {'line_number': 83, 'words_to_fix': {'begin'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = architecture.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '022')
        dExpected = [31]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = architecture.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '023')
        dExpected = ['2-10']
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = architecture.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '024')
        dExpected = [13,77]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025(self):
        oRule = architecture.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '025')
        self.assertFalse(oRule.fixable)

        dExpected = [3, 10, 17, 24]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)

        oRule.violations = []
        oRule.names = []
        oRule.names.append('rtl')
        dExpected = [10, 17, 24]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl')

        oRule.violations = []
        oRule.names = ['ENTITY1']
        dExpected = [3, 17, 24]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: entity1')

        oRule.violations = []
        oRule.names = ['BLUE']
        dExpected = [3, 10, 24]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: blue')

        oRule.violations = []
        oRule.names = ['CDC']
        dExpected = [3, 10, 17]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: cdc')

        oRule.violations = []
        oRule.names = ['rtl', 'CDC']
        dExpected = [10, 17]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl,cdc')

        oRule.violations = []
        oRule.names = ['rtl', 'cdc', 'blue']
        dExpected = [10]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl,cdc,blue')

        oRule.violations = []
        oRule.names = ['rtl', 'cdc', 'blue', 'entity1']
        dExpected = []
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl,cdc,blue,entity1')
