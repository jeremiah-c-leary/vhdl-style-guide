
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

        dExpected = [19,34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = entity.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([19,34])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = entity.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [utils.add_violation(34)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = entity.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [{'line_number': 19, 'words_to_fix': {'entITy'}},
                     {'line_number': 34, 'words_to_fix': {'eNTITY'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = entity.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [49]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_lowercase(self):
        oRule = entity.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [{'line_number': 19, 'words_to_fix': {'IS'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_uppercase(self):
        oRule = entity.rule_006()
        oRule.case = 'upper'

        dExpected = [{'line_number': 3, 'words_to_fix': {'is'}},
                     {'line_number': 34, 'words_to_fix': {'is'}},
                     {'line_number': 65, 'words_to_fix': {'is'}},
                     {'line_number': 80, 'words_to_fix': {'is'}},
                     {'line_number': 94, 'words_to_fix': {'is'}},
                     {'line_number': 113, 'words_to_fix': {'is'}},
                     {'line_number': 127, 'words_to_fix': {'is'}},
                     {'line_number': 138, 'words_to_fix': {'is'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = entity.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [19,34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [{'line_number': 19, 'words_to_fix': {'entiTY2'}},
                     {'line_number': 34, 'words_to_fix': {'entiTY3'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = entity.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [33,47]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = entity.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [{'line_number': 47, 'words_to_fix': {'END'}},
                     {'line_number': 63, 'words_to_fix': {'End'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = entity.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '011')

        dExpected = utils.add_violation_list([63,91])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_uppercase(self):
        oRule = entity.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [{'line_number': 33, 'words_to_fix': {'entiTY2'}},
                     {'line_number': 47, 'words_to_fix': {'entiTY3'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_lowercase(self):
        oRule = entity.rule_012()
        oRule.case = 'lower'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [{'line_number': 16, 'words_to_fix': {'ENTITY1'}},
                     {'line_number': 33, 'words_to_fix': {'entiTY2'}},
                     {'line_number': 47, 'words_to_fix': {'entiTY3'}},
                     {'line_number': 63, 'words_to_fix': {'ENTITY1'}},
                     {'line_number': 78, 'words_to_fix': {'ENTITY1'}},
                     {'line_number': 91, 'words_to_fix': {'ENTITY1'}},
                     {'line_number': 103, 'words_to_fix': {'ENT1'}},
                     {'line_number': 123, 'words_to_fix': {'ENTITY1'}},
                     {'line_number': 146, 'words_to_fix': {'ENTITY1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = entity.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '013')

        dExpected = utils.add_violation_list([33,63,123])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014_lowercase(self):
        oRule = entity.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '014')

        dExpected = [{'line_number': 47, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 78, 'words_to_fix': {'ENtity'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014_uppercase(self):
        oRule = entity.rule_014()
        oRule.case = 'upper'

        dExpected = [{'line_number': 16, 'words_to_fix': {'entity'}},
                     {'line_number': 33, 'words_to_fix': {'entity'}},
                     {'line_number': 63, 'words_to_fix': {'entity'}},
                     {'line_number': 78, 'words_to_fix': {'ENtity'}},
                     {'line_number': 91, 'words_to_fix': {'entity'}},
                     {'line_number': 123, 'words_to_fix': {'entity'}},
                     {'line_number': 133, 'words_to_fix': {'entity'}},
                     {'line_number': 146, 'words_to_fix': {'entity'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = entity.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [103]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = entity.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [33,146]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = entity.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '017')

        dExpected = ['8-15','25-31','39-46','56-62','70-77','86-90','98-102','118-122','128-132']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = entity.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '018')

        dExpected = ['19-33']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = entity.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '019')

        dExpected = [133]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
