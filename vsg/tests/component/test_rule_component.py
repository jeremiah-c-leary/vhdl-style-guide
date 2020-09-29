import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_comment_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(lFileComment)


class testRuleComponentMethods(unittest.TestCase):

    def test_rule_019(self):
        oRule = component.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'component')
        self.assertEqual(oRule.identifier, '019')

        dExpected = utils.add_violation_list([7,12,14])
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, dExpected)
