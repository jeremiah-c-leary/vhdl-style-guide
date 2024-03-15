
import os
import unittest

from vsg.rules import declarative_part
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_400_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400(self):
        oRule = declarative_part.rule_400()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'declarative_part')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [4, 5, 10, 19, 24, 29, 36, 45, 46, 51, 56, 63, 72, 73, 78, 83, 90, 99, 104, 109, 116, 126, 127, 132, 137, 144]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400(self):
        oRule = declarative_part.rule_400()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

