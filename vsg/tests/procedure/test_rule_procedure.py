import os

import unittest

from vsg.rules import procedure
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'procedure_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testRuleProcedureMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = procedure.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([14,16,40])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = procedure.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [utils.add_violation(41)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = procedure.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '003')
        dExpected = utils.add_violation_list([14,42])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = procedure.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([17,18,19,20,45,46,47,48])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = procedure.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '005')
        dExpected = utils.add_violation_list([89,90,115,116])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = procedure.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '006')
        dExpected = utils.add_violation_list([40, 98])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = procedure.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [{'lines': [{'number': 28}], 'words_to_fix': {'End'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = procedure.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [{'lines': [{'number': 28}], 'words_to_fix': {'PROCEDURE'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
