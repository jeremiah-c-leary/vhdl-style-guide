# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import entity

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "user_error_messages_input.vhd"))


class test_option(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_entity_008_without_user_message(self):
        oRule = entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "008")

        lExpected = [2]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)
        self.assertEqual(1, len(oRule.violations))
        self.assertEqual('Change "FIFO" to "fifo"', oRule.violations[0].sSolution)

    def test_rule_entity_008_with_user_message(self):
        oRule = entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "008")
        oRule.user_error_message = "This is a user error message."

        lExpected = [2]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)
        self.assertEqual(1, len(oRule.violations))
        self.assertEqual('Change "FIFO" to "fifo" [user_error_message: This is a user error message.]', oRule.violations[0].sSolution)
