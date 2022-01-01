
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_016_test_input.vhd'))


class test_process_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_016(self):
        oRule = process.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '016')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [15, 22, 36, 43]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
