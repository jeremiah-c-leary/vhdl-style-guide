
import sys
sys.path.append('..\..')
import unittest
import rule_library
import os


class testRuleLibraryMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = rule_library.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = rule_library.rule_001()

        dExpected = [2,4]
        lLines = []
        lLines.append('  This is a test of ending library')
        lLines.append(' library ')
        lLines.append('library')
        lLines.append('     Library  ')
        lLines.append('Library')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = rule_library.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = rule_library.rule_002()

        dExpected = [3,4]
        lLines = []
        lLines.append('  This is a test of ending library  this should pass')
        lLines.append(' library this_is_a_library')
        lLines.append('library  this_is_a_library')
        lLines.append('     Library    this_is_a_library')
        lLines.append('Library This_is_a_library')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = rule_library.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = rule_library.rule_003()

        dExpected = [2,5]
        lLines = []
        lLines.append('  This is a test of ending library  this should pass')
        lLines.append(' library this_is_a_library')
        lLines.append('')
        lLines.append('library  this_is_a_library')
        lLines.append('     Library    this_is_a_library')
        lLines.append('     ')
        lLines.append('Library This_is_a_library')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = rule_library.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004(self):
        oRule = rule_library.rule_004()

        dExpected = [5,7]
        lLines = []
        lLines.append('  This is a test of ending library  this should pass')
        lLines.append('     library this_is_a_lib')
        lLines.append('')
        lLines.append('library  this_is_a_lib')
        lLines.append('     Library    this_is_a_lib')
        lLines.append('     ')
        lLines.append('Library This_is_a_lib')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = rule_library.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '005')

    def test_rule_005(self):
        oRule = rule_library.rule_005()

        dExpected = [5,7]
        lLines = []
        lLines.append('  This is a test of ending use  this should pass')
        lLines.append('     use this_is_a_lib')
        lLines.append('')
        lLines.append('use  this_is_a_lib')
        lLines.append('     USE    this_is_a_lib')
        lLines.append('     ')
        lLines.append('Use This_is_a_lib')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = rule_library.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = rule_library.rule_006()

        dExpected = [4,5]
        lLines = []
        lLines.append('  This is a test of ending use  this should pass')
        lLines.append('     use this_is_a_lib')
        lLines.append('')
        lLines.append('use  this_is_a_lib')
        lLines.append('     USE    this_is_a_lib')
        lLines.append('     ')
        lLines.append('Use This_is_a_lib')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_exists(self):
        oRule = rule_library.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '007')

    def test_rule_007(self):
        oRule = rule_library.rule_007()

        dExpected = [4,7]
        lLines = []
        lLines.append('  This is a test of ending use  this should pass')
        lLines.append('     use this_is_a_lib')
        lLines.append('')
        lLines.append('use  this_is_a_lib')
        lLines.append('     USE    this_is_a_lib')
        lLines.append('     ')
        lLines.append('Use This_is_a_lib')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008_exists(self):
        oRule = rule_library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '008')

    def test_rule_008(self):
        oRule = rule_library.rule_008()

        dExpected = [4,6,7,9]
        lLines = []
        lLines.append('  This is a test of ending use  this should pass')
        lLines.append('  use this_is_a_lib')
        lLines.append('')
        lLines.append('use  this_is_a_lib')
        lLines.append('  USE    this_is_a_lib')
        lLines.append('   USE    this_is_a_lib')
        lLines.append('       USE    this_is_a_lib')
        lLines.append('     ')
        lLines.append(' Use This_is_a_lib')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

if __name__ == '__main__':
    unittest.main()
