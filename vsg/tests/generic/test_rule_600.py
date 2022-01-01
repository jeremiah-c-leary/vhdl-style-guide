
import os
import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_600_test_input.vhd'))


class test_generic_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_600(self):
        oRule = generic.rule_600()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '600')
        self.assertEqual(oRule.groups, ['naming'])

        lExpected = [14, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_600_g_uppercase(self):
        oRule = generic.rule_600()
        oRule.suffixes = ['_G']
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '600')

        lExpected = [14, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
