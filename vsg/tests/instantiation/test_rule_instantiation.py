import os

import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils


lFilePort = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_test_input.vhd'))
oFilePort = vhdlFile.vhdlFile(lFilePort)
lFileGeneric = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_generic_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(lFileGeneric)
lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_comment_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(lFileComment)
lFilePositional = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_positional_test_input.vhd'))
oFilePositional = vhdlFile.vhdlFile(lFilePositional)
lFileDirect = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_direct_test_input.vhd'))
oFileDirect = vhdlFile.vhdlFile(lFileDirect)

class testRuleInstantiationMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = instantiation.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '001')

        dExpected = utils.add_violation_list([19,21,25,26,27,31,32,33,34,35,37,42,44,52])
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = instantiation.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([44,52])
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = instantiation.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '003')

        dExpected = utils.add_violation_list([36,52])
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = instantiation.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '004')

        dExpected = utils.add_violation_list([23,29,36])
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = instantiation.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [52]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = instantiation.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [{'line_number': 31, 'words_to_fix': {'pOrt'}},
                     {'line_number': 37, 'words_to_fix': {'mAp'}},
                     {'line_number': 52, 'words_to_fix': {'mAp'}}]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = instantiation.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [55]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = instantiation.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [{'line_number': 17, 'words_to_fix': {'U_INsT1'}},
                     {'line_number': 52, 'words_to_fix': {'U_InST1'}}]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = instantiation.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '009')

        dExpected = [{'line_number': 23, 'words_to_fix': {'InST1'}},
                     {'line_number': 52, 'words_to_fix': {'INsT1'}}]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = instantiation.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '010')

        dExpected = ['18-22']
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = instantiation.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '011')

        dExpected = [{'line_number': 19, 'words_to_fix': {'port_1'}},
                     {'line_number': 20, 'words_to_fix': {'port_2'}},
                     {'line_number': 21, 'words_to_fix': {'port_3'}},
                     {'line_number': 25, 'words_to_fix': {'port_1'}},
                     {'line_number': 26, 'words_to_fix': {'port_2'}},
                     {'line_number': 27, 'words_to_fix': {'port_3'}},
                     {'line_number': 32, 'words_to_fix': {'port_1'}},
                     {'line_number': 33, 'words_to_fix': {'port_2'}},
                     {'line_number': 34, 'words_to_fix': {'port_3'}},
                     {'line_number': 39, 'words_to_fix': {'port_1'}},
                     {'line_number': 41, 'words_to_fix': {'port_3'}},
                     {'line_number': 46, 'words_to_fix': {'port_1'}},
                     {'line_number': 47, 'words_to_fix': {'port_2'}},
                     {'line_number': 48, 'words_to_fix': {'port_3'}},
                     {'line_number': 53, 'words_to_fix': {'port_1'}},
                     {'line_number': 54, 'words_to_fix': {'port_2'}},
                     {'line_number': 55, 'words_to_fix': {'port_3'}},
                     {'line_number': 71, 'words_to_fix': {'port_1'}},
                     {'line_number': 72, 'words_to_fix': {'port_2'}},
                     {'line_number': 95, 'words_to_fix': {'b'}}]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = instantiation.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '012')

        dExpected = [63]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = instantiation.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '013')

        dExpected = [{'line_number': 22, 'words_to_fix': {'genEric'}},
                     {'line_number': 33, 'words_to_fix': {'mAP'}}]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = instantiation.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '014')

        dExpected = [46,65,73,98]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = instantiation.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '015')

        dExpected = ['33-36','44-46','54-56']
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = instantiation.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '016')

        dExpected = [{'line_number': 34, 'words_to_fix': {'GENerIC_1'}},
                     {'line_number': 46, 'words_to_fix': {'GENERic_2'}},
                     {'line_number': 55, 'words_to_fix': {'generic_2'}}]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = instantiation.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [54]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001_generics(self):
        oRule = instantiation.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '001')

        dExpected = utils.add_violation_list([22,33,45,46,73])
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_018(self):
        oRule = instantiation.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '018')

        dExpected = utils.add_violation_list([26,33,54,66])
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_019(self):
        oRule = instantiation.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '019')

        dExpected = utils.add_violation_list([22,28,35,66])
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_020(self):
        oRule = instantiation.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '020')

        dExpected = [58]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = instantiation.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '021')

        dExpected = [65,77]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = instantiation.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '022')

        dExpected = [26,27]
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = instantiation.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '023')

        dExpected = [24,29,31]
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = instantiation.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '024')

        dExpected = [7,9,10,13,14]
        oRule.analyze(oFilePositional)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025(self):
        oRule = instantiation.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '025')

        dExpected = [utils.add_violation(81)]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_026(self):
        oRule = instantiation.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '026')

        dExpected = [utils.add_violation(86)]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_027(self):
        oRule = instantiation.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '027')

        dExpected = [{'line_number': 13, 'words_to_fix': {'ENTITY'}},
                     {'line_number': 20, 'words_to_fix': {'ENTITY'}}]
        oRule.analyze(oFileDirect)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_028(self):
        oRule = instantiation.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '028')

        dExpected = [{'line_number': 20, 'words_to_fix': {'inst1'}}]
        oRule.analyze(oFileDirect)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_029(self):
        oRule = instantiation.rule_029()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '029')
        lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_comment_test_input.vhd'))
        oFileComment = vhdlFile.vhdlFile(lFileComment)
        dExpected = ['22-32']
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_030(self):
        oRule = instantiation.rule_030()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '030')

        dExpected = [65,83]
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, dExpected)
