# -*- coding: utf-8 -*-
import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import comment, constant, entity, length, library, port

# Read in test file used for all tests
dIndentMap = utils.read_indent_file()

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__), "code_tag_test_input.vhd"))
oFile = vhdlFile.vhdlFile(lFile)
oFile.set_indent_map(dIndentMap)


class testCodeTags(unittest.TestCase):
    def setUp(self):
        self.assertIsNone(eError)

    def test_rule_library_001(self):
        oRule = library.rule_002()

        oRule.analyze(oFile)
        self.assertEqual(len(oRule.violations), 2)

    def test_rule_comment_010(self):
        oRule = comment.rule_010()

        oRule.analyze(oFile)
        self.assertEqual(len(oRule.violations), 0)

    def test_rule_constant_016(self):
        oRule = constant.rule_016()

        oRule.analyze(oFile)
        self.assertEqual(len(oRule.violations), 0)

    def test_rule_length_003(self):
        oRule = length.rule_003()
        oRule.length = 2

        oRule.analyze(oFile)
        self.assertEqual(len(oRule.violations), 1)
