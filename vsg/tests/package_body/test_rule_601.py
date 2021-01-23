
import os
import unittest

from vsg.rules import package_body
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_601_test_input.vhd'))


class test_package_body_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_601(self):
        oRule = package_body.rule_601()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'package_body')
        self.assertEqual(oRule.identifier, '601')

        lExpected = [6, 8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
