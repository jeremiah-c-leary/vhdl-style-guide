# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import pragma
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_402_test_input.vhd'))

dIndentMap = utils.read_indent_file()


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_default(self):
        oRule = pragma.rule_402()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'pragma')
        self.assertEqual(oRule.identifier, '402')

        lExpected = [11]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_default(self):
        oRule = pragma.rule_402()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_402_test_input.fixed_default.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
