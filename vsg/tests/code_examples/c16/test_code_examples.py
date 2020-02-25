import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

lBaudGen = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'BaudGen.vhd'))
oBaudGen = vhdlFile.vhdlFile(lBaudGen)
lBoardCpu = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'Board_cpu.vhd'))
oBoardCpu = vhdlFile.vhdlFile(lBoardCpu)
lDataCore = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'data_core.vhd'))
oDataCore = vhdlFile.vhdlFile(lDataCore)


class testCodeExample(unittest.TestCase):

    def test_baudgen(self):
        oRuleList = rule_list.rule_list(oBaudGen)
        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['separate_generic_port_alignment'] = False
        oRuleList.configure(dConfiguration)
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
