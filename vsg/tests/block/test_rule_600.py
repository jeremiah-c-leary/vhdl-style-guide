
import os
import unittest

from vsg.rules import block
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_600_test_input.vhd'))


class test_block_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_600(self):
        oRule = block.rule_600()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block')
        self.assertEqual(oRule.identifier, '600')

        lExpected = [8, 8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

