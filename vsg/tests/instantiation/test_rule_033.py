
import os
import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_033_test_input.vhd'))

lExpected_add = []
lExpected_add.append('')
utils.read_file(os.path.join(sTestDir, 'rule_033_test_input.fixed_add.vhd'), lExpected_add)

lExpected_remove = []
lExpected_remove.append('')
utils.read_file(os.path.join(sTestDir, 'rule_033_test_input.fixed_remove.vhd'), lExpected_remove)


class test_instantiation_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_033_add(self):
        oRule = instantiation.rule_033()
        oRule.action = 'add'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '033')
        self.assertEqual(oRule.groups, ['structure', 'structure::optional'])

        lExpected = [6, 29]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_033_add(self):
        oRule = instantiation.rule_033()
        oRule.action = 'add'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_033_remove(self):
        oRule = instantiation.rule_033()
        oRule.action = 'remove'

        lExpected = [22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_033_remove(self):
        oRule = instantiation.rule_033()
        oRule.action = 'remove'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
