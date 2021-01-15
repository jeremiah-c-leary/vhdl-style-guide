
import os
import unittest

from vsg.rules import port
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_011_test_input.vhd'))


class test_port_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_011(self):
        oRule = port.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '011')

        lExpected = [14, 15, 16, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
