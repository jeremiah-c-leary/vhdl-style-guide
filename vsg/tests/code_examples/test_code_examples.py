import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

oTimestamp = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'timestamp.vhdl'))
oSpiSlave = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'spi_slave.vhd'))
oSpiMaster = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'spi_master.vhd'))
oGrpDebouncer = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'grp_debouncer.vhd'))
oPIC = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'PIC.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_timestamp_vhdl(self):
        oRuleList = rule_list.rule_list(oTimestamp)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'timestamp.fixed.vhdl'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oTimestamp.lines[iLineNumber].line, sLine)

    def test_spi_slave(self):
        oRuleList = rule_list.rule_list(oSpiSlave)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_slave.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiSlave.lines[iLineNumber].line, sLine)

    def test_spi_master(self):
        oRuleList = rule_list.rule_list(oSpiMaster)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_master.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiMaster.lines[iLineNumber].line, sLine)

    def test_grp_debouncer(self):
        oRuleList = rule_list.rule_list(oGrpDebouncer)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'grp_debouncer.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oGrpDebouncer.lines[iLineNumber].line, sLine)

    def test_pic(self):
        oRuleList = rule_list.rule_list(oPIC)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'PIC.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oPIC.lines[iLineNumber].line, sLine)
