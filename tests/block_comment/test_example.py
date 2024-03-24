# -*- coding: utf-8 -*-
import os
import unittest

from tests import utils
from vsg import config, rule_list, severity, vhdlFile

sSourceCodeDir = os.path.dirname(__file__)

dIndentMap = utils.read_indent_file()

lExample = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'example.vhd'))
oExample = vhdlFile.vhdlFile(lExample[0])
oExample.set_indent_map(dIndentMap)

oConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'example_config.yaml'))

oSeverityList = severity.create_list({})

class testCodeExample(unittest.TestCase):

    def test_example(self):
        oRuleList = rule_list.rule_list(oExample, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'example.fixed.vhd'), lExpected)
        self.assertEqual(lExpected, oExample.get_lines())

        self.assertFalse(oRuleList.violations)
