
import os
import unittest

from vsg.rules import length
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))


class test_length_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_001_default(self):
        oRule = length.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'length')
        self.assertEqual(oRule.identifier, '001')

        lExpected = [3, 7, 9]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_with_125_characters(self):
        oRule = length.rule_001()
        oRule.length = 125

        lExpected = [3, 9]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

