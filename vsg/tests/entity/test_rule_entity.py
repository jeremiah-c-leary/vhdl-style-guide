
import os
import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','entity','entity_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testRuleEntityMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = entity.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '001')

        lExpected = [19,34]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_002(self):
        oRule = entity.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '002')

        lExpected = [19,34]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_003(self):
        oRule = entity.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [34]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_004(self):
        oRule = entity.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '004')

        lExpected = [19, 34]

        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_005(self):
        oRule = entity.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '005')

        lExpected = [50]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_006_lowercase(self):
        oRule = entity.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '006')

        lExpected = [19]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_006_uppercase(self):
        oRule = entity.rule_006()
        oRule.case = 'upper'

        lExpected = [3,34,50,65,80,94,113,127,138,150]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_007(self):
        oRule = entity.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '007')

        lExpected = [19,34]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_008(self):
        oRule = entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '008')

        lExpected = [19,34]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_009(self):
        oRule = entity.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '009')

        lExpected = [33,47]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_010(self):
        oRule = entity.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '010')

        lExpected = [47,63]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_011(self):
        oRule = entity.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '011')

        lExpected = [63,91]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_012_lowercase(self):
        oRule = entity.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '012')

        lExpected = [33,47,103]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_012_uppercase(self):
        oRule = entity.rule_012()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '012')

        lExpected = [16,33,47,63,78,91,123,146,160]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_013(self):
        oRule = entity.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '013')

        lExpected = [33,63,123]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_014_lowercase(self):
        oRule = entity.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '014')

        lExpected = [47,78]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_014_uppercase(self):
        oRule = entity.rule_014()
        oRule.case = 'upper'

        lExpected = [16,33,63,78,91,123,133,146,160]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_015(self):
        oRule = entity.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '015')

        lExpected = [103]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_016(self):
        oRule = entity.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '016')

        lExpected = [33,146]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))

    def test_rule_017(self):
        oRule = entity.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [{'lines': [{'number': 9, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 10, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 11, 'keyword_column': 13, 'before_keyword_column': 11},
                                {'number': 12, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 13, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 14, 'keyword_column': 10, 'before_keyword_column': 8}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11},
                     {'lines': [{'number': 21, 'keyword_column': 18, 'before_keyword_column': 16},
                                {'number': 22, 'keyword_column': 15, 'before_keyword_column': 13}],
                      'max_keyword_column': 18, 'max_before_keyword_column': 16},
                     {'lines': [{'number': 26, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 27, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 28, 'keyword_column': 13, 'before_keyword_column': 11},
                                {'number': 29, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 30, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 31, 'keyword_column': 10, 'before_keyword_column': 8}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11},
                     {'lines': [{'number': 40, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 41, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 42, 'keyword_column': 13, 'before_keyword_column': 11},
                                {'number': 43, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 44, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 45, 'keyword_column': 11, 'before_keyword_column': 9}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11},
                     {'lines': [{'number': 52, 'keyword_column': 15, 'before_keyword_column': 13},
                                {'number': 53, 'keyword_column': 13, 'before_keyword_column': 11}],
                      'max_keyword_column': 15, 'max_before_keyword_column': 13},
                     {'lines': [{'number': 57, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 58, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 59, 'keyword_column': 9, 'before_keyword_column': 7},
                                {'number': 60, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 61, 'keyword_column': 14, 'before_keyword_column': 12},
                                {'number': 62, 'keyword_column': 10, 'before_keyword_column': 8}],
                      'max_keyword_column': 14, 'max_before_keyword_column': 12},
                     {'lines': [{'number': 67, 'keyword_column': 15, 'before_keyword_column': 13},
                                {'number': 68, 'keyword_column': 14, 'before_keyword_column': 12}],
                      'max_keyword_column': 15, 'max_before_keyword_column': 13},
                     {'lines': [{'number': 71, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 72, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 73, 'keyword_column': 13, 'before_keyword_column': 11},
                                {'number': 74, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 75, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 76, 'keyword_column': 10, 'before_keyword_column': 8}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11},
                     {'lines': [{'number': 83, 'keyword_column': 17, 'before_keyword_column': 15},
                                {'number': 84, 'keyword_column': 15, 'before_keyword_column': 13}],
                      'max_keyword_column': 17, 'max_before_keyword_column': 15},
                     {'lines': [{'number': 87, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 88, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 89, 'keyword_column': 13, 'before_keyword_column': 11}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11},
                     {'lines': [{'number': 97, 'keyword_column': 15, 'before_keyword_column': 13},
                                {'number': 99, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 100, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 101, 'keyword_column': 13, 'before_keyword_column': 11}],
                      'max_keyword_column': 15, 'max_before_keyword_column': 13},
                     {'lines': [{'number': 119, 'keyword_column': 21, 'before_keyword_column': 19},
                                {'number': 120, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 121, 'keyword_column': 23, 'before_keyword_column': 21}],
                      'max_keyword_column': 23, 'max_before_keyword_column': 21},
                     {'lines': [{'number': 129, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 130, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 131, 'keyword_column': 13, 'before_keyword_column': 11}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = entity.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '018')

        dExpected = [{'lines': [{'number': 21, 'keyword_column': 30, 'before_keyword_column': 28},
                                {'number': 22, 'keyword_column': 27, 'before_keyword_column': 25}],
                      'max_keyword_column': 30, 'max_before_keyword_column': 28},
                     {'lines': [{'number': 52, 'keyword_column': 29, 'before_keyword_column': 27},
                                {'number': 53, 'keyword_column': 25, 'before_keyword_column': 23}],
                      'max_keyword_column': 29, 'max_before_keyword_column': 27}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = entity.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '019')

        lExpected = [133]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines(oRule.violations))
