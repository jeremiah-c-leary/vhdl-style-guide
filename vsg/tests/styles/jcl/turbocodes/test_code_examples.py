import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

dIndentMap = utils.read_indent_file()

lIteration, eError = vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','..','code_examples', 'turbocodes', 'iteration_synth.vhd'))
oIteration = vhdlFile.vhdlFile(lIteration)
oIteration.set_indent_map(dIndentMap)

oConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','..','styles', 'jcl.yaml'))

oSeverityList = severity.create_list({})


class testCodeExample(unittest.TestCase):

    def setUp(self):
        self.assertIsNone(eError)

    def test_iteration_synth(self):
        oRuleList = rule_list.rule_list(oIteration, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = ['']

        utils.read_file(os.path.join(os.path.dirname(__file__),'iteration_synth.fixed.vhd'), lExpected)

        self.assertEqual(lExpected, oIteration.get_lines())
