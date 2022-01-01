
import os
import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_020_test_input.vhd'))


class test_generic_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_020(self):
        oRule = generic.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '020')
        self.assertEqual(oRule.groups, ['naming'])

        lExpected = [14, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_020_w_uppercase(self):
        oRule = generic.rule_020()
        oRule.prefixes = ['G_']
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '020')

        lExpected = [14, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
