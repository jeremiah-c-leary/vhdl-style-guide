# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import port

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_605_test_input.vhd'))


class test_port_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_605(self):
        oRule = port.rule_605()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '605')

        lExpected = [21, 24, 26, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
