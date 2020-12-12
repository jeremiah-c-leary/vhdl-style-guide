
import os
import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_019_test_input.vhd'))

lExpected_add = []
lExpected_add.append('')
utils.read_file(os.path.join(sTestDir, 'rule_019_test_input.fixed_add.vhd'), lExpected_add)

lExpected_remove = []
lExpected_remove.append('')
utils.read_file(os.path.join(sTestDir, 'rule_019_test_input.fixed_remove.vhd'), lExpected_remove)


class test_entity_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_019_add(self):
        oRule = entity.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '019')

        lExpected = [9]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_019_add(self):
        oRule = entity.rule_019()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_019_remove(self):
        oRule = entity.rule_019()
        oRule.action = 'remove'

        lExpected = [4]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_019_remove(self):
        oRule = entity.rule_019()
        oRule.action = 'remove'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
