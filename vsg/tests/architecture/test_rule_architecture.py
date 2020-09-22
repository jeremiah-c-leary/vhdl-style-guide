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

    def test_rule_012(self):
        oRule = architecture.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([7,18])
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
        self.maxDiff = None
        oRule = architecture.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '027')
        dExpected = [{'lines': [{'number': 4, 'keyword_column': 34, 'before_keyword_column': 25},
                                {'number': 5, 'keyword_column': 30, 'before_keyword_column': 25},
                                {'number': 6, 'keyword_column': 28, 'before_keyword_column': 25},
                                {'number': 7, 'keyword_column': 35, 'before_keyword_column': 25},
                                {'number': 8, 'keyword_column': 27, 'before_keyword_column': 25}],
                      'max_keyword_column': 35, 'max_before_keyword_column': 25}]
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
