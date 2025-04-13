# -*- coding: utf-8 -*-

import unittest
from unittest import mock

from vsg import config, deprecated_rule, parser, rule, violation
from vsg.rules import option
from vsg.vhdlFile.extract import tokens


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version
        self.style = "indent_only"
        self.configuration = []
        self.debug = False
        self.fix_only = False


class testRuleMethods(unittest.TestCase):
    def test_rule_exists(self):
        oRule = rule.Rule()
        self.assertTrue(oRule)

    def test_rule_name(self):
        oRule = rule.Rule()
        self.assertFalse(oRule.name)
        oRule.name = "sName"
        self.assertEqual(oRule.name, "sName")

    def test_rule_id(self):
        oRule = rule.Rule()
        self.assertFalse(oRule.identifier)
        oRule.identifier = "rule id 001"
        self.assertEqual(oRule.identifier, "rule id 001")

    def test_rule_solution(self):
        oRule = rule.Rule()
        self.assertFalse(oRule.solution)
        oRule.solution = "rule solution"
        self.assertEqual(oRule.solution, "rule solution")

    def test_add_violations_method(self):
        oRule = rule.Rule()
        self.assertEqual(oRule.violations, [])

        oTokens = tokens.New(0, 0, [])
        oViolation = violation.New(0, oTokens, "")

        oRule.add_violation(oViolation)
        self.assertEqual(len(oRule.violations), 1)
        oRule.add_violation(oViolation)
        oRule.add_violation(oViolation)
        self.assertEqual(len(oRule.violations), 3)

    def test_fix_violation(self):
        oRule = rule.Rule()
        oTokens = tokens.New(0, 0, [])
        oViolation = violation.New(0, oTokens, "")

        self.assertIsNone(oRule._fix_violation(oViolation))

    @mock.patch("sys.stdout")
    def test_print_debug_message(self, mock_stdout):
        oRule = rule.Rule()
        oRule.set_debug()
        sString = "This is a debug message"

        lExpected = []
        lExpected.append(mock.call("INFO: This is a debug message"))

        oRule._print_debug_message(sString)

        mock_stdout.write.assert_has_calls(lExpected)

    def test_get_configuration(self):
        oRule = rule.Rule()
        oRule.name = "xyz"
        oRule.identifier = "010"
        oRule.phase = 3
        dExpected = {}
        dExpected["disable"] = False
        dExpected["fixable"] = True
        dExpected["indent_size"] = 2
        dExpected["indent_style"] = "spaces"
        dExpected["phase"] = 3
        dExpected["severity"] = "Error"
        dExpected["user_error_message"] = ""
        dActual = oRule.get_configuration()
        for sKey in dExpected.keys():
            self.assertEqual(dActual[sKey], dExpected[sKey])
        for sKey in dActual.keys():
            self.assertEqual(dActual[sKey], dExpected[sKey])

    def test_get_solution(self):
        oRule = rule.Rule()

        oTokens = tokens.New(0, 0, [])
        oViolation = violation.New(0, oTokens, "Solution Line 0")

        oRule.add_violation(oViolation)

        oViolation = violation.New(1, oTokens, "Solution Line 1")
        oRule.add_violation(oViolation)

        self.assertEqual(oRule._get_solution(0), "Solution Line 0")
        self.assertEqual(oRule._get_solution(1), "Solution Line 1")

    def test_get_violations_w_vsg_output_method(self):
        oRule = rule.Rule()
        oRule.name = "xyz"
        oRule.identifier = "001"
        oRule.solution = "Solution"

        self.assertFalse(oRule.has_violations())

        oToken = parser.item("first")
        oTokens = tokens.New(0, 1, [oToken])

        oViolation = violation.New(1, oTokens, "First")
        oRule.add_violation(oViolation)

        oToken = parser.item("second")
        oTokens = tokens.New(1, 2, [oToken])

        oViolation = violation.New(2, oTokens, "Second")
        oRule.add_violation(oViolation)

        oToken = parser.item("third")
        oTokens = tokens.New(2, 3, [oToken])

        oViolation = violation.New(3, oTokens, "Third")
        oRule.add_violation(oViolation)

        dActual = oRule.get_violations_at_linenumber(1)
        self.assertEqual("First", dActual[0]["solution"])

        dActual = oRule.get_violations_at_linenumber(2)
        self.assertEqual("Second", dActual[0]["solution"])

    def test_has_violations_method(self):
        oRule = rule.Rule()

        self.assertFalse(oRule.has_violations())

        oTokens = tokens.New(0, 0, [])

        oViolation = violation.New(0, oTokens, "")
        oRule.add_violation(oViolation)
        self.assertTrue(oRule.has_violations())

    def test_deprecated_rule(self):
        oRule = deprecated_rule.Rule()
        oRule.unique_id = "some_rule_001"
        oRule.message = ["This has been deprecated."]

        oConfig = config.New(command_line_args())

        dConfig = {}
        dConfig["rule"] = {}
        dConfig["rule"]["some_rule_001"] = {}
        dConfig["rule"]["some_rule_001"]["disable"] = True

        oConfig.dConfig = dConfig

        lExpected = []
        lExpected.append("ERROR [config-001] Rule some_rule_001 has been deprecated.")
        lExpected.append("  " + oRule.message[0])

        lActual = oRule.configure(oConfig)

        self.assertEqual(lExpected, lActual)

    def test_option_object_can_be_created(self):
        oOption = option.New("option_name")
