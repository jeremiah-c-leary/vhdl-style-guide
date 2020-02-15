import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_comment_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(lFileComment)


class testRuleComponentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = component.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [27,45]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = component.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([27,45])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = component.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '003')

        dExpected = utils.add_violation_list([5,66])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = component.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [{'line_number': 16, 'words_to_fix': {'comPOnent'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = component.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [27,78]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = component.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [{'line_number': 16, 'words_to_fix': {'Is'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = component.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [36]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = component.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [{'line_number': 16, 'words_to_fix': {'CORm1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = component.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [34,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = component.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [{'line_number': 23, 'words_to_fix': {'eNd'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = component.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '011')

        dExpected = [utils.add_violation(52)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_uppercase(self):
        oRule = component.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [{'line_number': 23, 'words_to_fix': {'CoMP1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_lowercase(self):
        oRule = component.rule_012()
        oRule.case = 'lower'

        dExpected = [{'line_number': 12, 'words_to_fix':{'COMP1'}},
                     {'line_number': 23, 'words_to_fix': {'CoMP1'}},
                     {'line_number': 34, 'words_to_fix': {'COMP1'}},
                     {'line_number': 52, 'words_to_fix': {'COMP1'}},
                     {'line_number': 65, 'words_to_fix': {'COMP1'}},
                     {'line_number': 75, 'words_to_fix': {'COMP1'}},
                     {'line_number': 87, 'words_to_fix': {'COMP1'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = component.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [utils.add_violation(34)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = component.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '014')

        dExpected = [{'line_number': 23, 'words_to_fix': {'comPonent'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_rule_015(self):
#        oRule = component.rule_015()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'component')
#        self.assertEqual(oRule.identifier, '015')
#
#        dExpected = [43]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = component.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [65]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = component.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '017')

        dExpected = ['37-42']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = component.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '018')

        dExpected = utils.add_violation_list([65,87])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = component.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '019')

        dExpected = [7,12,14]
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = component.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '020')

        dExpected = ['5-16']
        lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_comment_test_input.vhd'))
        oFileComment = vhdlFile.vhdlFile(lFileComment)
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)
