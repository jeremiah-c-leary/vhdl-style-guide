import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

sSourceDir = os.path.join(os.path.dirname(__file__),'..','..','code_examples','c16')

dIndentMap = utils.read_indent_file()

lBaudGen, eBaudGenError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'BaudGen.vhd'))
oBaudGen = vhdlFile.vhdlFile(lBaudGen)
oBaudGen.set_indent_map(dIndentMap)

lBoardCpu, eBoardCpuError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'Board_cpu.vhd'))
oBoardCpu = vhdlFile.vhdlFile(lBoardCpu)
oBoardCpu.set_indent_map(dIndentMap)

lDataCore, eDataCoreError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'data_core.vhd'))
oDataCore = vhdlFile.vhdlFile(lDataCore)
oDataCore.set_indent_map(dIndentMap)

dLegacyConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','..','styles', 'indent_only.yaml'))
dLegacyConfig['debug'] = False

oSeverityList = severity.create_list({})


class testCodeExample(unittest.TestCase):

    def setUp(self):
        self.assertIsNone(eBaudGenError)
        self.assertIsNone(eBoardCpuError)
        self.assertIsNone(eDataCoreError)

    def test_baudgen(self):
        oRuleList = rule_list.rule_list(oBaudGen, oSeverityList)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'BaudGen.vhd'), lExpected)
        self.assertEqual(lExpected, oBaudGen.get_lines())

    def test_board_cpu(self):
        oRuleList = rule_list.rule_list(oBoardCpu, oSeverityList)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Board_cpu.vhd'), lExpected)
        self.assertEqual(lExpected, oBoardCpu.get_lines())

    def test_data_core(self):
        oRuleList = rule_list.rule_list(oDataCore, oSeverityList)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'data_core.vhd'), lExpected)
        self.assertEqual(lExpected, oDataCore.get_lines())
