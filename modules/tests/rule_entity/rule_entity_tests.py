
import sys
sys.path.append('..\..')
import unittest
import rule_entity
import os


class testRuleEntityMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = rule_entity.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = rule_entity.rule_001()

        dExpected = [2,4]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append(' entity ')
        lLines.append('entity')
        lLines.append('     Entity  ')
        lLines.append('Entity')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = rule_entity.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = rule_entity.rule_002()

        dExpected = [3,5]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append(' entity blah is')
        lLines.append('entity  blah   is')
        lLines.append('     Entity blah    is  ')
        lLines.append('Entity   blah is')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = rule_entity.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = rule_entity.rule_003()

        dExpected = [4,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah is')
        lLines.append('entity  blah   is')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah    is  ')
        lLines.append('Entity   blah is')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = rule_entity.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004(self):
        oRule = rule_entity.rule_004()

        dExpected = [7,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah   is')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah    is  ')
        lLines.append('Entity   blah IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = rule_entity.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '005')

    def test_rule_005(self):
        oRule = rule_entity.rule_005()

        dExpected = [4,7]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah  ')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah    ')
        lLines.append('Entity   blah IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = rule_entity.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = rule_entity.rule_006()

        dExpected = [3,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah is  ')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('Entity   blah IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_exists(self):
        oRule = rule_entity.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '007')

    def test_rule_007(self):
        oRule = rule_entity.rule_007()

        dExpected = [4,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah   is  ')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('Entity   blah   IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
