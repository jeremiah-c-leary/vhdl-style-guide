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

    def test_rule_020(self):
        oRule = process.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '020')
        dExpected = utils.add_violation_list([19,25,26])
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
