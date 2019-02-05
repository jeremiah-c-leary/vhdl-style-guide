import unittest
import subprocess
import os

from vsg import vhdlFile
from vsg import rule_list


class testVsg(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile('vsg/tests/rule_list/entity_architecture.vhd')
        oRules = rule_list.rule_list(self.oFile, 'vsg/tests/rule_list/local_rules')

    def test_importing_local_rule(self):
        for oRule in oRules.rules:
            print oRule.name + '_' + oRule.identifier
