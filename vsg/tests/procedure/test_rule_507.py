
import os
import unittest

from vsg.rules import procedure
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_507_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_507_test_input.fixed.vhd'), lExpected)


class test_procedure_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_507(self):
        oRule = procedure.rule_507()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '507')
        self.assertEqual(oRule.groups, ['case'])

        lExpected = [8, 13, 14, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_507(self):
        oRule = procedure.rule_507()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
