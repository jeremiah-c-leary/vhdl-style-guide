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

    def test_rule_012(self):
        oRule = process.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([51,57])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

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
