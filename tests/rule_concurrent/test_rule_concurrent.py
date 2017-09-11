
import unittest
from modules import rule_concurrent
from modules import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile('tests/rule_concurrent/concurrent_test_input.vhd')

class testRuleConcurrentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_concurrent.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [7,11,24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_concurrent.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [7,8,24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_concurrent.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [28,29,30]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
