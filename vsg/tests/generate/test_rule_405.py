
import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_405_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_405_test_input.fixed.vhd'), lExpected)


class test_generate_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_405(self):
        oRule = generate.rule_405()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '405')

        lExpected = []
        lExpected.extend(range(46, 51))
        lExpected.extend(range(56, 61))
        lExpected.extend(range(66, 71))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_405(self):
        oRule = generate.rule_405()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
