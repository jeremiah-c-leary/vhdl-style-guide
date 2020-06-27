import os

import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileEvent = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'process_event_test_input.vhd'))
oFileEvent = vhdlFile.vhdlFile(lFileEvent)
lFileSensitivity = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_single_signal_sensivity_test_input.vhd'))
oFileSensitivity = vhdlFile.vhdlFile(lFileSensitivity)

class testRuleProcessMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = process.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([17,24,32,38,46])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = process.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([17,24])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = process.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '003')
        dExpected = utils.add_violation_list([20,40])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = process.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '004')
        lExpected = []
        dViolation = utils.add_violation(20)
        dViolation['words_to_fix'] = {'begIN'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['words_to_fix'] = {'beGIn'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = process.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '005')
        lExpected = []
        dViolation = utils.add_violation(17)
        dViolation['words_to_fix'] = {'prOCess'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(24)
        dViolation['words_to_fix'] = {'Process'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(32)
        dViolation['words_to_fix'] = {'proCEss'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_006(self):
        oRule = process.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '006')
        dExpected = utils.add_violation_list([9,15,22,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = process.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '007')
        dExpected = utils.add_violation_list([15,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = process.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '008')
        lExpected = []
        dViolation = utils.add_violation(15)
        dViolation['words_to_fix'] = {'eNd'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(36)
        dViolation['words_to_fix'] = {'End'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_009(self):
        oRule = process.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '009')
        lExpected = []
        dViolation = utils.add_violation(22)
        dViolation['words_to_fix'] = {'proCEss'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(42)
        dViolation['words_to_fix'] = {'Process'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_010(self):
        oRule = process.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [utils.add_violation(6)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = process.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [utils.add_violation(42)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = process.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([51,57])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = process.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '013')
        lExpected = []
        dViolation = utils.add_violation(6,)
        dViolation['words_to_fix'] = {'IS'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(27)
        dViolation['words_to_fix'] = {'iS'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['words_to_fix'] = {'Is'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_014(self):
        oRule = process.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '014')
        dExpected = utils.add_violation_list([19,33,39])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = process.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [utils.add_violation(63)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = process.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '016')
        dExpected = utils.add_violation_list([6,11,17,24,32,38,51,55,125])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = process.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '017')
        lExpected = [{'lines':[{'number': 63}], 'words_to_fix': {'END_PROC_NAME'}},
                     {'lines':[{'number': 68}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 75}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 81}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 88}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 97}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 116}], 'words_to_fix': {'MAIN'}},
                     {'lines':[{'number': 140}], 'words_to_fix': {'TEST_PROCESS'}},
                     {'lines':[{'number': 152}], 'words_to_fix': {'TEST'}},
                     {'lines':[{'number': 157}], 'words_to_fix': {'TEST_PROCESS_W_FUNCTION'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_018(self):
        oRule = process.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '018')
        lExpected = []
        lExpected.append(utils.add_violation(9))
        lExpected.append(utils.add_violation(15))
        lExpected.append(utils.add_violation(22))
        lExpected.append(utils.add_violation(30))
        lExpected.append(utils.add_violation(36))
        lExpected.append(utils.add_violation(42))
        lExpected.append(utils.add_violation(53))
        lExpected.append(utils.add_violation(60))
        lExpected.append(utils.add_violation(132))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_019(self):
        oRule = process.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '019')
        lExpected = [{'lines':[{'number': 65}], 'words_to_fix': {'END_PROC_NAME'}},
                     {'lines':[{'number': 72}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 79}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 86}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 94}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 103}], 'words_to_fix': {'PROC_NAME'}},
                     {'lines':[{'number': 123}], 'words_to_fix': {'MAIN'}},
                     {'lines':[{'number': 150}], 'words_to_fix': {'TEST_PROCESS'}},
                     {'lines':[{'number': 155}], 'words_to_fix': {'TEST'}},
                     {'lines':[{'number': 167}], 'words_to_fix': {'TEST_PROCESS_W_FUNCTION'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_020(self):
        oRule = process.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '020')
        dExpected = utils.add_violation_list([19,25,26])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_021(self):
        oRule = process.rule_021()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '021')
        dExpected = utils.add_violation_list([59,70])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_022(self):
        oRule = process.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '022')
        dExpected = utils.add_violation_list([20,47,52,59,64])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_023(self):
        oRule = process.rule_023()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '023')
        dExpected = utils.add_violation_list([9,22,48,53,60,65])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_024(self):
        oRule = process.rule_024()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '024')
        dExpected = [utils.add_violation(63)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_025(self):
        oRule = process.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '025')
        dExpected = [utils.add_violation(68)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_026(self):
        oRule = process.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '026')
        dExpected = [utils.add_violation(75)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_027(self):
        oRule = process.rule_027()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '027')
        dExpected = utils.add_violation_list([77,84])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_028(self):
        oRule = process.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '028')
        dExpected = utils.add_violation_list([27,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_029_default_event(self):
        oRule = process.rule_029()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '029')
        self.assertEqual(oRule.clock, 'event')
        dExpected = utils.add_violation_list([9,13,34,44])
        oRule.analyze(oFileEvent)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(0), 'Use \'event for clocks.')

    def test_rule_029_edge(self):
        oRule = process.rule_029()
        oRule.clock = 'edge'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '029')
        dExpected = utils.add_violation_list([17, 21, 38,50])
        oRule.analyze(oFileEvent)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(0), 'Use rising_edge or falling_edge for clocks.')

    def test_rule_030(self):
        oRule = process.rule_030()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '030')
        dExpected = utils.add_violation_list([26,34])
        oRule.analyze(oFileSensitivity)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_036_with_default(self):
        oRule = process.rule_036()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '036')
        lExpected = utils.add_violation_list([63, 116, 140, 152, 157])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_036_with_override(self):
        oRule = process.rule_036()
        oRule.prefixes = ['test_', 'p']
        lExpected = utils.add_violation_list([63, 116, 152])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)
