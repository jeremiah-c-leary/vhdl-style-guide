import os

import unittest

from vsg.rules import library
from vsg.rules import entity
from vsg.rules import port
from vsg import vhdlFile


# Read in test file used for all tests

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__), 'code_tag_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testCodeTags(unittest.TestCase):

    def setUp(self):
        self.assertIsNone(eError)

    def test_rule_library_001(self):
        oRule = library.rule_002()

        oRule.analyze(oFile)
        self.assertEqual(len(oRule.violations), 2)

#    def test_rule_library_008(self):
#        oRule = library.rule_008()
#
#        dExpected = []
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_entity_019_enclosed_with_vsg_off_and_vsg_on(self):
#        oRule = entity.rule_019()
#
#        dExpected = []
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_rule_port_007(self):
#        oRule = port.rule_007()
#
#        dExpected = []
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
