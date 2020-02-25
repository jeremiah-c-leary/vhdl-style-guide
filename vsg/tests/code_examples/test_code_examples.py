import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

lTimestamp = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'timestamp.vhdl'))
oTimestamp = vhdlFile.vhdlFile(lTimestamp)

lSpiSlave = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'spi_slave.vhd'))
oSpiSlave = vhdlFile.vhdlFile(lSpiSlave)

lSpiMaster = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'spi_master.vhd'))
oSpiMaster = vhdlFile.vhdlFile(lSpiMaster)

lGrpDebouncer = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'grp_debouncer.vhd'))
oGrpDebouncer = vhdlFile.vhdlFile(lGrpDebouncer)

lPIC = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'PIC.vhd'))
oPIC = vhdlFile.vhdlFile(lPIC)

lIdentifier = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','identifier_alignment_input.vhd'))
oIdentifier = vhdlFile.vhdlFile(lIdentifier)

class testVhdlFileMethods(unittest.TestCase):

    @unittest.skip("This test should be done for example configurations only.")
    def test_timestamp_vhdl(self):
        oRuleList = rule_list.rule_list(oTimestamp)
        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['comment_line_ends_group'] = False
        oRuleList.configure(dConfiguration)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'timestamp.fixed.vhdl'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oTimestamp.lines[iLineNumber].line, sLine)

    @unittest.skip("This test should be done for example configurations only.")
    def test_spi_slave(self):
        oRuleList = rule_list.rule_list(oSpiSlave)
        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['comment_line_ends_group'] = False
        dConfiguration['rule']['global']['separate_generic_port_alignment'] = True
        oRuleList.configure(dConfiguration)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_slave.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiSlave.lines[iLineNumber].line, sLine)

    @unittest.skip("This test should be done for example configurations only.")
    def test_spi_master(self):
        oRuleList = rule_list.rule_list(oSpiMaster)
        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['comment_line_ends_group'] = False
        dConfiguration['rule']['global']['compact_alignment'] = False
        oRuleList.configure(dConfiguration)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_master.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiMaster.lines[iLineNumber].line, sLine)

    @unittest.skip("This test should be done for example configurations only.")
    def test_grp_debouncer(self):
        oRuleList = rule_list.rule_list(oGrpDebouncer)
        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['compact_alignment'] = False
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'grp_debouncer.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oGrpDebouncer.lines[iLineNumber].line, sLine)

    @unittest.skip("This test should be done for example configurations only.")
    def test_pic(self):
        oRuleList = rule_list.rule_list(oPIC)
        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['compact_alignment'] = False
        oRuleList.configure(dConfiguration)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'PIC.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oPIC.lines[iLineNumber].line, sLine)

    @unittest.skip("This test should be done for example configurations only.")
    def test_identifier(self):
        oRuleList = rule_list.rule_list(oIdentifier)
        oRuleList.fix(7)
#        utils.debug_lines(oIdentifier, 1, 20)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'identifier_alignment_input.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oIdentifier.lines[iLineNumber].line, sLine)

