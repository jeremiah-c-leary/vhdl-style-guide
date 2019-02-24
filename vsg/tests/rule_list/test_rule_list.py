import unittest

from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils


class testVsg(unittest.TestCase):

    def setUp(self):
        self.lFile = utils.read_vhdlfile('vsg/tests/rule_list/entity_architecture.vhd')
        self.oFile = vhdlFile.vhdlFile(self.lFile) 
        oRules = rule_list.rule_list(self.oFile, 'vsg/tests/rule_list/local_rules')

    def test_importing_local_rule(self):
        for oRule in oRules.rules:
            print oRule.name + '_' + oRule.identifier
