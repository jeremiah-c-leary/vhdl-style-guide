
import os
import unittest

from vsg.rules import generic_map
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_008_test_input.vhd'))


class test_generic_map_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_008(self):
        oRule = generic_map.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic_map')
        self.assertEqual(oRule.identifier, '008')

        lExpected = [23, 33, 35]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
