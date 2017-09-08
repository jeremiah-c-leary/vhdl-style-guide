
import sys
sys.path.append('..\..')
import unittest
import rule_entity
import os


# Read in test file used for all tests
lLines = []
with open('entity_test_input.vhd') as oFile:
    for sLine in oFile:
        lLines.append(sLine.rstrip())
oFile.close()


class testRuleEntityMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_entity.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [19,34]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_entity.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [19,34]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_entity.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [34]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = rule_entity.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [19,34]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = rule_entity.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [49]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = rule_entity.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [19]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = rule_entity.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [19,34]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = rule_entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [25,56]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = rule_entity.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [39,56]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = rule_entity.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '010')

        dExpected = [25,56]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = rule_entity.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '011')

        dExpected = [27,29,43,45,57,59,61]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = rule_entity.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [29,40,60]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = rule_entity.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [27,30,44,58]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = rule_entity.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '014')

        dExpected = [12,26,29,40,43,57,60,74]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = rule_entity.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '015')

        dExpected = [13,30,41,44,61,75]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = rule_entity.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [28,45,59,62]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = rule_entity.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [19,34]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = rule_entity.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '018')

        dExpected = [33,47]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = rule_entity.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '019')

        dExpected = [47,63]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = rule_entity.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '020')

        dExpected = [63,91]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = rule_entity.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '021')

        dExpected = [33,47]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = rule_entity.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '022')

        dExpected = [12,13,14,26,27,28,40,41,42,60,61,62,74,75,76]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023_prefix(self):
        oRule = rule_entity.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '023')
        oRule.port_direction = 'Prefix'

        dExpected = [12,13,14,29,30,31,43,44,45,60,61,62,74,75,76,99,100,101]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023_none(self):
        oRule = rule_entity.rule_023()
        oRule.port_direction = None

        dExpected = []
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023_suffix(self):
        oRule = rule_entity.rule_023()
        oRule.port_direction = 'Suffix'

        dExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,120, 129,130,131]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = rule_entity.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '024')

        dExpected = [33,63]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025(self):
        oRule = rule_entity.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '025')

        dExpected = [46,77]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_026(self):
        oRule = rule_entity.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '026')

        dExpected = [82]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_027(self):
        oRule = rule_entity.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '027')

        dExpected = [51,66]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_028(self):
        oRule = rule_entity.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '028')

        dExpected = [51,82]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_029(self):
        oRule = rule_entity.rule_029()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '029')

        dExpected = [21,53,68,83]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_030(self):
        oRule = rule_entity.rule_030()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '030')

        dExpected = [36,37,52,67,84]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_031(self):
        oRule = rule_entity.rule_031()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '031')

        dExpected = [21,37,52,53,68,83]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_032(self):
        oRule = rule_entity.rule_032()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '032')

        dExpected = [22,36,37,67]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_033(self):
        oRule = rule_entity.rule_033()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '033')

        dExpected = [85,117]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_034(self):
        oRule = rule_entity.rule_034()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '034')

        dExpected = [66,82,95]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_035(self):
        oRule = rule_entity.rule_035()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '035')

        dExpected = [25,39]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_036(self):
        oRule = rule_entity.rule_036()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '036')

        dExpected = [43,58,75]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_037(self):
        oRule = rule_entity.rule_037()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '037')

        dExpected = [119,121]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_038(self):
        oRule = rule_entity.rule_038()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '038')

        dExpected = [33,63,123]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_039(self):
        oRule = rule_entity.rule_039()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '039')

        dExpected = [47,78]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_040(self):
        oRule = rule_entity.rule_040()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '040')

        dExpected = [25,56,98]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_041(self):
        oRule = rule_entity.rule_041()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '041')

        dExpected = [67,96,116]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_042(self):
        oRule = rule_entity.rule_042()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '042')

        dExpected = [103]
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
