
import os
import unittest

from vsg import vhdlFile

from vsg.rules import with_statement
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, 'rule_001_test_input.vhd'))


class test_with_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.assertIsNone(eError)

    def test_rule_001(self):
        oRule = with_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'with')
        self.assertEqual(oRule.identifier, '001')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
