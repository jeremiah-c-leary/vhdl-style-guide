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

        dExpected = utils.add_violation_list([9,20])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = architecture.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = architecture.rule_002()

        dExpected = [utils.add_violation(14)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = architecture.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = architecture.rule_003()

        dExpected = [utils.add_violation(14)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = architecture.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004_lowercase(self):
        oRule = architecture.rule_004()

        dExpected = [{'lines':[{'number': 20}], 'words_to_fix': {'Architecture'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_uppercase(self):
        oRule = architecture.rule_004()
        oRule.case = 'upper'

        dExpected = [{'lines':[{'number': 3}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 9}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 14}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 20}], 'words_to_fix': {'Architecture'}},
                    {'lines':[{'number': 26}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 33}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 37}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 47}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 59}], 'words_to_fix': {'architecture'}},
                    {'lines':[{'number': 81}], 'words_to_fix': {'architecture'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = architecture.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = architecture.rule_006()

        dExpected = utils.add_violation_list([2,9])
        oRule.analyze(oFileIs)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = architecture.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [utils.add_violation(22)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = architecture.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '008')
        dExpected = utils.add_violation_list([24,31])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = architecture.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [{'lines':[{'number': 7}], 'words_to_fix': {'End'}},
                     {'lines':[{'number': 24}], 'words_to_fix': {'eND'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = architecture.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '010')
        dExpected = utils.add_violation_list([55,77])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_architecture_end(self):
        oRule = architecture.rule_010()
        dExpected = []
        oRule.analyze(oFileEnd)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_uppercase(self):
        oRule = architecture.rule_011()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [{'lines':[{'number': 24}], 'words_to_fix': {'ArCh'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_lowercase(self):
        oRule = architecture.rule_011()
        dExpected = [{'lines':[{'number': 7}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 18}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 24}], 'words_to_fix': {'ArCh'}},
                     {'lines':[{'number': 31}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 35}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 45}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 55}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 85}], 'words_to_fix': {'ARCH'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = architecture.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([7,18])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013_uppercase(self):
        oRule = architecture.rule_013()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [{'lines':[{'number': 3}], 'words_to_fix': {'Arch'}},
                     {'lines':[{'number': 20}], 'words_to_fix': {'ARch'}},
                     {'lines':[{'number': 26}], 'words_to_fix': {'ARch'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013_lowercase(self):
        oRule = architecture.rule_013()
        dExpected = [{'lines':[{'number': 3}], 'words_to_fix': {'Arch'}},
                     {'lines':[{'number': 9}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 14}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 20}], 'words_to_fix': {'ARch'}},
                     {'lines':[{'number': 26}], 'words_to_fix': {'ARch'}},
                     {'lines':[{'number': 33}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 37}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 47}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 59}], 'words_to_fix': {'ARCH'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'ARCH'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014_uppercase(self):
        oRule = architecture.rule_014()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '014')
        dExpected = [{'lines':[{'number': 9}], 'words_to_fix': {'EntITY'}},
                     {'lines':[{'number': 20}], 'words_to_fix': {'entity'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'ent'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014_lowercase(self):
        oRule = architecture.rule_014()
        dExpected = [{'lines':[{'number': 3}], 'words_to_fix': {'ENTITY'}},
                     {'lines':[{'number': 9}], 'words_to_fix': {'EntITY'}},
                     {'lines':[{'number': 14}], 'words_to_fix': {'ENTITY'}},
                     {'lines':[{'number': 33}], 'words_to_fix': {'ENTITY'}},
                     {'lines':[{'number': 37}], 'words_to_fix': {'ENTITY'}},
                     {'lines':[{'number': 47}], 'words_to_fix': {'ENTITY'}},
                     {'lines':[{'number': 59}], 'words_to_fix': {'ENTITY'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = architecture.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '015')
        dExpected = utils.add_violation_list([26,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = architecture.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '016')
        dExpected = [utils.add_violation(34)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = architecture.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '017')
        dExpected = [utils.add_violation(34)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = architecture.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '018')
        dExpected = [utils.add_violation(35)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019_lowercase(self):
        oRule = architecture.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '019')
        dExpected = [{'lines':[{'number': 20}], 'words_to_fix': {'Of'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019_uppercase(self):
        oRule = architecture.rule_019()
        oRule.case = 'upper'
        dExpected = [{'lines':[{'number': 3}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 9}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 14}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 20}], 'words_to_fix': {'Of'}},
                     {'lines':[{'number': 33}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 37}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 47}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 59}], 'words_to_fix': {'of'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'of'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_lowercase(self):
        oRule = architecture.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '020')
        dExpected = [{'lines':[{'number': 20}], 'words_to_fix': {'Is'}},
                     {'lines':[{'number': 33}], 'words_to_fix': {'iS'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020_uppercase(self):
        oRule = architecture.rule_020()
        oRule.case = 'upper'
        dExpected = [{'lines':[{'number': 3}], 'words_to_fix': {'is'}},
                     {'lines':[{'number': 9}], 'words_to_fix': {'is'}},
                     {'lines':[{'number': 14}], 'words_to_fix': {'is'}},
                     {'lines':[{'number': 20}], 'words_to_fix': {'Is'}},
                     {'lines':[{'number': 33}], 'words_to_fix': {'iS'}},
                     {'lines':[{'number': 37}], 'words_to_fix': {'is'}},
                     {'lines':[{'number': 47}], 'words_to_fix': {'is'}},
                     {'lines':[{'number': 59}], 'words_to_fix': {'is'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'is'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021_lowercase(self):
        oRule = architecture.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '021')
        dExpected = [{'lines':[{'number': 29}], 'words_to_fix': {'BEGIN'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021_uppercase(self):
        oRule = architecture.rule_021()
        oRule.case = 'upper'
        dExpected = [{'lines':[{'number': 5}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 11}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 16}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 22}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 34}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 39}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 49}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 61}], 'words_to_fix': {'begin'}},
                     {'lines':[{'number': 83}], 'words_to_fix': {'begin'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = architecture.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '022')
        dExpected = [utils.add_violation(31)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = architecture.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '024')
        lExpected = []
        dViolation = utils.add_violation(13)
        dViolation['label'] = 'ARCH'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(77)
        dViolation['label'] = 'ARCH'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_025(self):
        oRule = architecture.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '025')
        self.assertFalse(oRule.fixable)

        dExpected = utils.add_violation_list([3, 10, 17, 24])
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)

        oRule.violations = []
        oRule.names = []
        oRule.names.append('rtl')
        dExpected = utils.add_violation_list([10, 17, 24])
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl')

        oRule.violations = []
        oRule.names = ['ENTITY1']
        dExpected = utils.add_violation_list([3, 17, 24])
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: entity1')

        oRule.violations = []
        oRule.names = ['BLUE']
        dExpected = utils.add_violation_list([3, 10, 24])
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: blue')

        oRule.violations = []
        oRule.names = ['CDC']
        dExpected = utils.add_violation_list([3, 10, 17])
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: cdc')

        oRule.violations = []
        oRule.names = ['rtl', 'CDC']
        dExpected = utils.add_violation_list([10, 17])
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl,cdc')

        oRule.violations = []
        oRule.names = ['rtl', 'cdc', 'blue']
        dExpected = [utils.add_violation(10)]
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl,cdc,blue')

        oRule.violations = []
        oRule.names = ['rtl', 'cdc', 'blue', 'entity1']
        dExpected = []
        oRule.analyze(oFileName)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(100), 'Architecture name must be from this list: rtl,cdc,blue,entity1')

    def test_rule_027(self):
        oRule = architecture.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '027')
        dExpected = [{'lines': [{'number': 4, 'keyword_column': 14, 'before_keyword_column': 5},
                                {'number': 5, 'keyword_column': 11, 'before_keyword_column': 5},
                                {'number': 6, 'keyword_column': 9, 'before_keyword_column': 5},
                                {'number': 7, 'keyword_column': 16, 'before_keyword_column': 5},
                                {'number': 8, 'keyword_column': 8, 'before_keyword_column': 5}],
                      'max_keyword_column': 16, 'max_before_keyword_column': 5}]
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_028(self):
        oRule = architecture.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '028')
        dExpected = [{'lines':[{'number': 13}], 'words_to_fix': {'Architecture'}},
                     {'lines':[{'number': 31}], 'words_to_fix': {'archITecture'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
