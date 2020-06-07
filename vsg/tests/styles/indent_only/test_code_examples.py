import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

sSourceCodeDir = os.path.join(os.path.dirname(__file__),'..','code_examples')

lTimestamp = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'timestamp.vhdl'))
oTimestamp = vhdlFile.vhdlFile(lTimestamp)

lSpiSlave = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'spi_slave.vhd'))
oSpiSlave = vhdlFile.vhdlFile(lSpiSlave)

lSpiMaster = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'spi_master.vhd'))
oSpiMaster = vhdlFile.vhdlFile(lSpiMaster)

lGrpDebouncer = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'grp_debouncer.vhd'))
oGrpDebouncer = vhdlFile.vhdlFile(lGrpDebouncer)

lPIC = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'PIC.vhd'))
oPIC = vhdlFile.vhdlFile(lPIC)

dLegacyConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','styles', 'indent_only.yaml'))

class testCodeExample(unittest.TestCase):

    def test_timestamp_vhdl(self):
        oRuleList = rule_list.rule_list(oTimestamp)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'timestamp.vhdl'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oTimestamp.lines[iLineNumber].line, sLine)

    def test_spi_slave(self):
        oRuleList = rule_list.rule_list(oSpiSlave)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_slave.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiSlave.lines[iLineNumber].line, sLine)

    def test_spi_master(self):
        oRuleList = rule_list.rule_list(oSpiMaster)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_master.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiMaster.lines[iLineNumber].line, sLine)

    def test_grp_debouncer(self):
        oRuleList = rule_list.rule_list(oGrpDebouncer)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'grp_debouncer.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oGrpDebouncer.lines[iLineNumber].line, sLine)

    def test_pic(self):
        oRuleList = rule_list.rule_list(oPIC)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'PIC.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oPIC.lines[iLineNumber].line, sLine)
