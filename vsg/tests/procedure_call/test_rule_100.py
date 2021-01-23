
import os
import unittest

from vsg.rules import procedure_call
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_100_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_100_test_input.fixed.vhd'), lExpected, False)


class test_procedure_call_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_100(self):
        oRule = procedure_call.rule_100()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure_call')
        self.assertEqual(oRule.identifier, '100')

        lExpected = [19,19, 21, 21, 21, 23, 23, 25, 25, 30, 30, 32, 32]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_100(self):
        oRule = procedure_call.rule_100()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
