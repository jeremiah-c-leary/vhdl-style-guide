
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_025_test_input.vhd'))


class test_architecture_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_025(self):
        oRule = architecture.rule_025()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '025')
        self.assertFalse(oRule.fixable)
        self.assertEqual(oRule.groups, ['naming'])

        lExpected = [3, 10, 17, 24]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: ', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = []
        oRule.names.append('rtl')
        lExpected = [10, 17, 24]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: rtl', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = ['ENTITY1']
        lExpected = [3, 17, 24]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: ENTITY1', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = ['BLUE']
        lExpected = [3, 10, 24]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: BLUE', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = ['CDC']
        lExpected = [3, 10, 17]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: CDC', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = ['rtl', 'CDC']
        lExpected = [10, 17]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: rtl, CDC', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = ['rtl', 'cdc', 'blue']
        lExpected = [10]
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: rtl, cdc, blue', oRule._get_solution(100))

        oRule.violations = []
        oRule.names = ['rtl', 'cdc', 'blue', 'entity1']
        lExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Architecture identifier must be from this list: rtl, cdc, blue, entity1', oRule._get_solution(100))

