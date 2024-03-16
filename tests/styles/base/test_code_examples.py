# -*- coding: utf-8 -*-
import os
import unittest

from tests import utils
from vsg import config, rule_list, severity, vhdlFile

sSourceCodeDir = os.path.join(os.path.dirname(__file__),'..','code_examples')

dIndentMap = utils.read_indent_file()

lNestedGenerates, eNestedGeneratesError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'nested_generates.vhd'))
oNestedGenerates = vhdlFile.vhdlFile(lNestedGenerates)
oNestedGenerates.set_indent_map(dIndentMap)

oConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','vsg','styles', 'jcl.yaml'))

oSeverityList = severity.create_list({})

class testCodeExample(unittest.TestCase):

    def setUp(self):
        self.assertIsNone(eNestedGeneratesError)

    def test_nested_generates(self):
        oRuleList = rule_list.rule_list(oNestedGenerates, oSeverityList)
#        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'nested_generates.fixed.vhd'), lExpected)

        self.assertEqual(lExpected, oNestedGenerates.get_lines())

