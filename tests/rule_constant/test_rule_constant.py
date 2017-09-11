
import unittest
from modules import rule_constant
from modules import vhdlFile


# Read in test file used for all tests

oFile = vhdlFile.vhdlFile('tests/rule_constant/constant_test_input.vhd')

class testRuleEntityMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_constant.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [8,9,10]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_constant.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [7,8]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_constant.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [7]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = rule_constant.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [8]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = rule_constant.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [8,9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = rule_constant.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [10]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = rule_constant.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [10]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = rule_constant.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [6,9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = rule_constant.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [5,6,8,9,10]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
