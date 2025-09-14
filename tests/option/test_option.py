# -*- coding: utf-8 -*-
import sys
import unittest
from unittest import mock

from vsg import __main__, config, deprecated_rule, parser, rule, violation
from vsg.rules import option
from vsg.rules.entity import rule_001
from vsg.vhdlFile.extract import tokens


class testRuleMethods(unittest.TestCase):
    def setUp(self):
        self.sOptionName = "option_name"
        self.oOption = option.New(self.sOptionName)
        self.oOption.value = "yes"

        self.oRule = rule.Rule()
        self.oRule.add_option(self.oOption)

    def test_option_object_can_be_created(self):
        self.assertEqual(self.oOption.name, self.sOptionName)

    def test_option_value(self):
        self.assertEqual(self.oOption.value, "yes")

    def test_option_name_added_to_rule_configuration(self):
        self.assertTrue(self.sOptionName in self.oRule.configuration)
        self.assertEqual(self.oRule.options[0].name, self.sOptionName)

    def test_option_reports_in_rc_command(self):
        dExpected = {}
        dExpected["indent_style"] = "spaces"
        dExpected["indent_size"] = 2
        dExpected["phase"] = None
        dExpected["disable"] = False
        dExpected["fixable"] = True
        dExpected["severity"] = "Error"
        dExpected["option_name"] = "yes"
        dExpected["user_error_message"] = ""

        dActual = self.oRule.get_configuration()

        self.assertEqual(dExpected, dActual)

    def test_option_is_configurable(self):
        self.oRule.name = "example"
        self.oRule.identifier = "001"

        dConfig = {}
        dConfig["rule"] = {}
        dConfig["rule"]["example_001"] = {}
        dConfig["rule"]["example_001"]["option_name"] = "no"

        oConfig = config.config()
        oConfig.dConfig = dConfig

        self.assertEqual(self.oRule.option_name, "yes")
        self.assertEqual(self.oRule.options[0].value, "yes")

        self.oRule.configure(oConfig)

        self.assertEqual(self.oRule.option_name, "no")
        self.assertEqual(self.oRule.options[0].value, "no")
