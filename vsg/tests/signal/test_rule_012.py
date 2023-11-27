
import os
import unittest

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_012_test_input.vhd'))


class test_signal_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = 'yes'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '012')
        self.assertEqual(oRule.groups, ['alignment'])

        lExpected = [4, 5, 10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = 'yes'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_yes.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = 'no'

        lExpected = [4, 5, 10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = 'no'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_no.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
