# -*- coding: utf-8 -*-
import copy
import os
import unittest

from tests import utils
from vsg import config, rule_list, severity, vhdlFile

sSourceCodeDir = os.path.join(os.path.dirname(__file__), "..", "code_examples")

dIndentMap = utils.read_indent_file()

lTimestamp, eTimestapError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "timestamp.vhd"))
oTimestamp = vhdlFile.vhdlFile(lTimestamp)
oTimestamp.set_indent_map(dIndentMap)

lSpiSlave, eSpiSlaveError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "spi_slave.vhd"))
oSpiSlave = vhdlFile.vhdlFile(lSpiSlave)
oSpiSlave.set_indent_map(dIndentMap)

lSpiMaster, eSpiMasterError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "spi_master.vhd"))
oSpiMaster = vhdlFile.vhdlFile(lSpiMaster)
oSpiMaster.set_indent_map(dIndentMap)

lGrpDebouncer, eGrpDebouncerError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "grp_debouncer.vhd"))
oGrpDebouncer = vhdlFile.vhdlFile(lGrpDebouncer)
oGrpDebouncer.set_indent_map(dIndentMap)

lPIC, ePICError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "PIC.vhd"))
oPIC = vhdlFile.vhdlFile(lPIC)
oPIC.set_indent_map(dIndentMap)

lLibraryStatements, eLibraryStatementsError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "library_statements.vhd"))
oLibraryStatements = vhdlFile.vhdlFile(lLibraryStatements)
oLibraryStatements.set_indent_map(dIndentMap)

lAlignments, eAlignmentsError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "alignments.vhd"))
oAlignments = vhdlFile.vhdlFile(lAlignments)
oAlignments.set_indent_map(dIndentMap)

lTrailingWhitespace, eAlignmentsError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "trailing_whitespace.vhd"))
oTrailingWhitespace = vhdlFile.vhdlFile(lTrailingWhitespace)
oTrailingWhitespace.set_indent_map(dIndentMap)

lComments, eCommentsError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "comments.vhd"))
oComments = vhdlFile.vhdlFile(lComments)
oComments.set_indent_map(dIndentMap)

lDeclarativePart, eDeclarativePartError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "..", "..", "declarative_part", "rule_400_test_input.vhd"))
oDeclarativePart = vhdlFile.vhdlFile(lDeclarativePart)
oDeclarativePart.set_indent_map(dIndentMap)

lTokenMovement, eTokenMovementError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceCodeDir, "token_movements.vhd"))
oTokenMovement = vhdlFile.vhdlFile(lTokenMovement)
oTokenMovement.set_indent_map(dIndentMap)

oConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__), "..", "..", "..", "vsg", "styles", "jcl.yaml"))

oSeverityList = severity.create_list({})


class testCodeExample(unittest.TestCase):
    def setUp(self):
        self.assertIsNone(eTimestapError)
        self.assertIsNone(eSpiSlaveError)
        self.assertIsNone(eSpiMasterError)
        self.assertIsNone(eGrpDebouncerError)
        self.assertIsNone(ePICError)
        self.assertIsNone(eLibraryStatementsError)
        self.assertIsNone(eCommentsError)
        self.assertIsNone(eDeclarativePartError)
        self.assertIsNone(eTokenMovementError)

    def test_timestamp_vhdl(self):
        oRuleList = rule_list.rule_list(oTimestamp, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "timestamp.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oTimestamp.get_lines())

    def test_spi_slave(self):
        self.maxDiff = None
        oRuleList = rule_list.rule_list(oSpiSlave, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()
        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "spi_slave.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oSpiSlave.get_lines())

    def test_spi_master(self):
        oRuleList = rule_list.rule_list(oSpiMaster, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "spi_master.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oSpiMaster.get_lines())

    def test_grp_debouncer(self):
        oRuleList = rule_list.rule_list(oGrpDebouncer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "grp_debouncer.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oGrpDebouncer.get_lines())

    def test_pic(self):
        oRuleList = rule_list.rule_list(oPIC, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "PIC.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oPIC.get_lines())

    def test_library_statements(self):
        oRuleList = rule_list.rule_list(oLibraryStatements, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "library_statements.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oLibraryStatements.get_lines())

        self.assertFalse(oRuleList.violations)
        oRuleList.check_rules()
        self.assertFalse(oRuleList.violations)

    def test_alignments(self):
        oRuleList = rule_list.rule_list(oAlignments, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "alignments.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oAlignments.get_lines())

        self.assertFalse(oRuleList.violations)
        oRuleList.check_rules()
        self.assertFalse(oRuleList.violations)

    def test_trailing_whitespace(self):
        oRuleList = rule_list.rule_list(oTrailingWhitespace, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "trailing_whitespace.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oTrailingWhitespace.get_lines())

        self.assertFalse(oRuleList.violations)
        oRuleList.check_rules()
        self.assertFalse(oRuleList.violations)

    def test_comments(self):
        oRuleList = rule_list.rule_list(oComments, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "comments.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oComments.get_lines())

        self.assertFalse(oRuleList.violations)
        oRuleList.check_rules()
        self.assertFalse(oRuleList.violations)

    def test_declarative_part(self):
        oRuleList = rule_list.rule_list(oDeclarativePart, oSeverityList)
        oMyConfig = copy.deepcopy(oConfig)
        oMyConfig.dConfig["rule"]["architecture_601"] = {}
        oMyConfig.dConfig["rule"]["architecture_601"]["disable"] = True
        oMyConfig.dConfig["rule"]["signal_007"] = {}
        oMyConfig.dConfig["rule"]["signal_007"]["disable"] = True
        oMyConfig.dConfig["rule"]["variable_007"] = {}
        oMyConfig.dConfig["rule"]["variable_007"]["disable"] = True
        oMyConfig.dConfig["rule"]["process_016"] = {}
        oMyConfig.dConfig["rule"]["process_016"]["disable"] = True
        oMyConfig.dConfig["rule"]["process_018"] = {}
        oMyConfig.dConfig["rule"]["process_018"]["disable"] = True
        oMyConfig.dConfig["rule"]["entity_016"] = {}
        oMyConfig.dConfig["rule"]["entity_016"]["disable"] = True
        oRuleList.configure(oMyConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "rule_400_test_input.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oDeclarativePart.get_lines())

        self.assertFalse(oRuleList.violations)
        oRuleList.check_rules()
        self.assertFalse(oRuleList.violations)

    def test_token_movement(self):
        oRuleList = rule_list.rule_list(oTokenMovement, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix()

        lExpected = [""]
        utils.read_file(os.path.join(os.path.dirname(__file__), "token_movements.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, oTokenMovement.get_lines())
