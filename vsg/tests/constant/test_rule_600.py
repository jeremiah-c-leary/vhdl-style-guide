
import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_600_test_input.vhd'))


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_600(self):
        oRule = constant.rule_600()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '600')

        lExpected = [5, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_600_with_override(self):
        oRule = constant.rule_600()
        oRule.suffixes = ['_x']
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '600')

        lExpected = [4, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
