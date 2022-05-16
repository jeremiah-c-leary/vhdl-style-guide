
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_401_test_input.vhd'))

lExpected_all = []
lExpected_all.append('')
utils.read_file(os.path.join(sTestDir, 'rule_401_test_input.fixed.vhd'), lExpected_all)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_401(self):
        oRule = process.rule_401()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '401')

        lExpected = [17, 19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401(self):
        oRule = process.rule_401()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
