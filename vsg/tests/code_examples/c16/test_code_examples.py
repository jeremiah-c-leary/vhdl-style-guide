import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

oBaudGen = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'BaudGen.vhd'))
oBoardCpu = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'Board_cpu.vhd'))
oDataCore = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'data_core.vhd'))


class testCodeExample(unittest.TestCase):

    def test_baudgen(self):
        oRuleList = rule_list.rule_list(oBaudGen)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'BaudGen.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oBaudGen.lines[iLineNumber].line, sLine)

    def test_board_cpu(self):
        oRuleList = rule_list.rule_list(oBoardCpu)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Board_cpu.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oBoardCpu.lines[iLineNumber].line, sLine)

    def test_data_core(self):
        oRuleList = rule_list.rule_list(oDataCore)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'data_core.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oDataCore.lines[iLineNumber].line, sLine)
