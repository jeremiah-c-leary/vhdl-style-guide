# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import variable
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_011_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_011_test_input.fixed.vhd'), lExpected)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_011(self):
        self.maxDiff = None
        oRule = variable.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '011')

        lExpected = [22, 22, 22, 22, 24, 28, 29, 32]
        lExpected.extend([47, 47, 47, 47, 50])
        lExpected.extend([86, 86, 86, 86, 88])
        lExpected.extend([104, 104, 104, 104, 106])
        lExpected.extend([113, 113, 113, 113, 116])
        lExpected.extend([139, 139, 139, 139, 142])
        lExpected.extend([157, 157, 157, 157, 160])
        lExpected.extend([167, 167, 167, 167, 169])
        lExpected.extend([204, 204, 204, 204, 206])
        lExpected.extend([222, 222, 222, 222, 224, 225])
        lExpected.extend([231, 231, 231, 231, 234, 235])
        lExpected.extend([259, 259, 259, 259, 262])
        lExpected.extend([277, 277, 277, 277, 280])
        lExpected.extend([287, 287, 287, 287, 290])
        lExpected.extend([321, 321, 321, 321, 324])
        lExpected.extend([331, 331, 331, 331, 334])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011(self):
        oRule = variable.rule_011()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
