import os

import unittest

from vsg.rules import library
from vsg.rules import entity
from vsg.rules import port
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests

oFile = vhdlFile.vhdlFile(vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'code_tag_test_input.vhd')))

class testCodeTags(unittest.TestCase):

    def test_rule_library_008(self):
        oRule = library.rule_008()

        dExpected = []
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_entity_019_enclosed_with_vsg_off_and_vsg_on(self):
        oRule = entity.rule_019()

        dExpected = []
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_port_007(self):
        oRule = port.rule_007()

        dExpected = []
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
