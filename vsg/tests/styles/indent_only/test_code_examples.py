import os
import unittest

from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

sSourceCodeDir = os.path.join(os.path.dirname(__file__),'..','code_examples')

dIndentMap = utils.read_indent_file()

lTimestamp, eTimestampError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'timestamp.vhdl'))
oTimestamp = vhdlFile.vhdlFile(lTimestamp)
oTimestamp.set_indent_map(dIndentMap)

lSpiSlave, eSpiSlaveError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'spi_slave.vhd'))
oSpiSlave = vhdlFile.vhdlFile(lSpiSlave)
oSpiSlave.set_indent_map(dIndentMap)

lSpiMaster, eSpiMasterError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'spi_master.vhd'))
oSpiMaster = vhdlFile.vhdlFile(lSpiMaster)
oSpiMaster.set_indent_map(dIndentMap)

lGrpDebouncer, eGrpDebouncerError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'grp_debouncer.vhd'))
oGrpDebouncer = vhdlFile.vhdlFile(lGrpDebouncer)
oGrpDebouncer.set_indent_map(dIndentMap)

lPIC, ePICError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir,'PIC.vhd'))
oPIC = vhdlFile.vhdlFile(lPIC)
oPIC.set_indent_map(dIndentMap)

oConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','styles', 'indent_only.yaml'))

oSeverityList = severity.create_list({})


class testCodeExample(unittest.TestCase):

    def setUp(self):
        self.assertIsNone(eTimestampError)
        self.assertIsNone(eSpiSlaveError)
        self.assertIsNone(eSpiMasterError)
        self.assertIsNone(eGrpDebouncerError)
        self.assertIsNone(ePICError)

    def test_timestamp_vhdl(self):
        oRuleList = rule_list.rule_list(oTimestamp, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'timestamp.vhdl'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oTimestamp.get_lines())

    def test_spi_slave(self):
        oRuleList = rule_list.rule_list(oSpiSlave, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_slave.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oSpiSlave.get_lines())

    def test_spi_master(self):
        oRuleList = rule_list.rule_list(oSpiMaster, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_master.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oSpiMaster.get_lines())

    def test_grp_debouncer(self):
        oRuleList = rule_list.rule_list(oGrpDebouncer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'grp_debouncer.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oGrpDebouncer.get_lines())

    def test_pic(self):
        oRuleList = rule_list.rule_list(oPIC, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'PIC.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oPIC.get_lines())
