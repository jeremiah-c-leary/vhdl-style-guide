# -*- coding: utf-8 -*-
import json
import unittest

from tests import utils
from vsg import rule_list, severity, vhdlFile

dIndentMap = utils.read_indent_file()

oSeverityList = severity.create_list({})


class testVsg(unittest.TestCase):

    def test_extract_violation_dictionary(self):
#        self.maxDiff = None
        lFile = []
        utils.read_file('tests/styles/code_examples/spi_master.vhd', lFile)
        oFile = vhdlFile.vhdlFile(lFile)
        oFile.set_indent_map(dIndentMap)
        oRules = rule_list.rule_list(oFile, oSeverityList)
        oRules.check_rules()
        with open('tests/rule_list/extract_violation_dictionary.json') as jsonFile:
            dExpected = json.load(jsonFile)
        self.assertEqual(dExpected, oRules.extract_violation_dictionary())

    def test_extract_violation_dictionary_w_all_phases_enabled(self):
#        self.maxDiff = None
        lFile = []
        utils.read_file('tests/styles/code_examples/spi_master.vhd', lFile)
        oFile = vhdlFile.vhdlFile(lFile)
        oFile.set_indent_map(dIndentMap)
        oRules = rule_list.rule_list(oFile, oSeverityList)
        oRules.check_rules(True)
        with open('tests/rule_list/extract_violation_dictionary_w_all_phases_enabled.json') as jsonFile:
            dExpected = json.load(jsonFile)
        self.assertEqual(dExpected, oRules.extract_violation_dictionary())
