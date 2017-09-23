
import unittest
import sys
sys.path.append('modules')

from modules.rules import rule_instantiation
from modules import vhdlFile


oFile = vhdlFile.vhdlFile('tests/rule_instantiation/instantiation_test_input.vhd')


class testRuleInstantiationMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_instantiation.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [19,21,25,26,27,31,32,33,34,35,37,42,44,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_instantiation.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [36,44,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_instantiation.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [36,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = rule_instantiation.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '004')
 
        dExpected = [23,29,36]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = rule_instantiation.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = rule_instantiation.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [31,37,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = rule_instantiation.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [55]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = rule_instantiation.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [17,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = rule_instantiation.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [23,52]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = rule_instantiation.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '010')

        dExpected = ['18-22']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = rule_instantiation.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '011')

        dExpected = [19,20,21,25,26,27,32,33,34,39,40,41,46,47,48,53,54,55]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_rule_012(self):
#        oRule = rule_instantiation.rule_012()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'instantiation')
#        self.assertEqual(oRule.identifier, '012')
#
#        dExpected = [23]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_013(self):
#        oRule = rule_instantiation.rule_013()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'instantiation')
#        self.assertEqual(oRule.identifier, '013')
#
#        dExpected = [34]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_014(self):
#        oRule = rule_instantiation.rule_014()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'instantiation')
#        self.assertEqual(oRule.identifier, '014')
#
#        dExpected = [23]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_015(self):
#        oRule = rule_instantiation.rule_015()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'instantiation')
#        self.assertEqual(oRule.identifier, '015')
#
#        dExpected = [43]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_016(self):
#        oRule = rule_instantiation.rule_016()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'instantiation')
#        self.assertEqual(oRule.identifier, '016')
#
#        dExpected = [65]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_017(self):
#        oRule = rule_instantiation.rule_017()
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'instantiation')
#        self.assertEqual(oRule.identifier, '017')
#
#        dExpected = ['37-42']
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
