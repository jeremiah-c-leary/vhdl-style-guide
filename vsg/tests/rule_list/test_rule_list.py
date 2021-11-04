import unittest
import json

from vsg import vhdlFile
from vsg import rule_list
from vsg import severity

from vsg.tests import utils

dIndentMap = utils.read_indent_file()

oSeverityList = severity.create_list({})


class testVsg(unittest.TestCase):

    @unittest.skip('Skipping just for hotfix release 3.3.1.')
    def test_extract_violation_dictionary(self):
        self.maxDiff = None
        lFile = []
        utils.read_file('vsg/tests/styles/code_examples/spi_master.vhd', lFile)
        oFile = vhdlFile.vhdlFile(lFile)
        oFile.set_indent_map(dIndentMap)
        oRules = rule_list.rule_list(oFile, oSeverityList)
        oRules.check_rules()
        with open('vsg/tests/rule_list/extract_violation_dictionary.json') as jsonFile:
            dExpected = json.load(jsonFile)
        self.assertEqual(dExpected, oRules.extract_violation_dictionary())

    @unittest.skip('Skipping just for hotfix release 3.3.1.')
    def test_extract_violation_dictionary_w_all_phases_enabled(self):
        self.maxDiff = None
        lFile = []
        utils.read_file('vsg/tests/styles/code_examples/spi_master.vhd', lFile)
        oFile = vhdlFile.vhdlFile(lFile)
        oFile.set_indent_map(dIndentMap)
        oRules = rule_list.rule_list(oFile, oSeverityList)
        oRules.check_rules(True)
        with open('vsg/tests/rule_list/extract_violation_dictionary_w_all_phases_enabled.json') as jsonFile:
            dExpected = json.load(jsonFile)
        self.assertEqual(dExpected, oRules.extract_violation_dictionary())
