import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_test_input.vhd'))
lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_comment_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(lFileComment)


class testFixRuleComponentMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_019(self):
        oRule = component.rule_019()
        oRule.fix(oFileComment)
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileComment.lines[7].line, '      generic_1 : std_logic := \'0\';')
        self.assertEqual(oFileComment.lines[12].line, '      port_2 : in    std_logic;')
        self.assertEqual(oFileComment.lines[14].line, '      port_4 : out   std_logic')
