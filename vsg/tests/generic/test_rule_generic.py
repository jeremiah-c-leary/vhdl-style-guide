import os

import unittest

from vsg.rules import generic
from vsg import vhdlFile


oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'generic_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'generic_multiple_on_one_line_test_input.vhd'))
oFileComponent = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'generic_component_test_input.vhd'))

class testRuleGenericMethods(unittest.TestCase):


    def test_rule_001(self):
        oRule = generic.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [82]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = generic.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [51,66]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = generic.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [51,82]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = generic.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [21,53,68,83]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = generic.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [36,37,52,67,84]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = generic.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [37,52,53,68,83]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_component_rule_006(self):
        oRule = generic.rule_006()

        dExpected = [36,37]
        oRule.analyze(oFileComponent)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = generic.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [22,36,37,67]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = generic.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [85,117]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = generic.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [66,82,95]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = generic.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [97]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_rule_011(self):
#        oRule = generic.rule_011()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'generic')
#        self.assertEqual(oRule.identifier, '011')
#
#        dExpected = [67,96,116]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = generic.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '012')

        dExpected = ['20-23','51-54','66-69','82-85']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = generic.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [139]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = generic.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '014')

        dExpected = [68,116]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = generic.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '015')

        dExpected = ['20-23','51-54','66-69']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = generic.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

        oRule.violations = []
        dExpected = [5]
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = generic.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [52,96]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

