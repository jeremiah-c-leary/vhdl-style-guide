# -*- coding: utf-8 -*-
import glob
import os
import unittest
from tempfile import TemporaryDirectory

from tests import utils
from vsg import __rule_doc_gen__, rule_list, vhdlFile


class testDocGen(unittest.TestCase):
    @classmethod
    def compare_files(cls, sRuleName):
        lExpected = []
        utils.read_file(os.path.join("docs", f"{sRuleName}_rules.rst"), lExpected, bStrip=False)
        lActual = []
        utils.read_file(os.path.join(cls._tmpdir.name, f"{sRuleName}_rules.rst"), lActual, bStrip=False)

        return lExpected, lActual

    @classmethod
    def setUpClass(cls):
        cls._tmpdir = TemporaryDirectory()
        __rule_doc_gen__.create_rule_documentation(cls._tmpdir.name)

    @classmethod
    def tearDownClass(cls):
        cls._tmpdir.cleanup()

    def test_documentation_links_in_docstrings(self):
        oVhdlFile = vhdlFile.vhdlFile([""])
        oRuleList = rule_list.rule_list(oVhdlFile, None, None)
        lExpected = []
        lActual = []

        for oRule in oRuleList.rules:
            if oRule.configuration_documentation_link is None:
                continue
            lExpected.append(oRule.unique_id)
            if "|" + oRule.configuration_documentation_link + "|" in oRule.__doc__:
                lActual.append(oRule.unique_id)

        self.assertEqual(lExpected, lActual)

    def test_rule_link_in_configuration_documentation_exists(self):
        self.maxDiff = None
        oVhdlFile = vhdlFile.vhdlFile([""])
        oRuleList = rule_list.rule_list(oVhdlFile, None, None)
        lExpected = []
        lActual = []

        dConfigurationFiles = {}
        for oRule in oRuleList.rules:
            if oRule.configuration_documentation_link is None:
                continue
            dConfigurationFiles[oRule.configuration_documentation_link] = []

        for oRule in oRuleList.rules:
            if oRule.configuration_documentation_link is None:
                continue
            dConfigurationFiles[oRule.configuration_documentation_link].append(oRule.unique_id)

        for sKey in list(dConfigurationFiles.keys()):
            if sKey == "configuring_prefix_and_suffix_rules_link":
                continue
            if sKey.endswith("_link"):
                sFileName = sKey[: -len("_link")] + ".rst"
                sFullPathFileName = os.path.join("docs", sFileName)
            lFile = []
            utils.read_file(sFullPathFileName, lFile)
            lActual = []
            bStartProcessing = False
            for sLine in lFile:
                if bStartProcessing:
                    if sLine.startswith("*"):
                        lLine = sLine.split()
                        lActual.append(lLine[1][1:])
                if sLine.startswith("Rules Enforcing"):
                    bStartProcessing = True
            self.assertEqual(dConfigurationFiles[sKey], lActual)

    def test_rule_link_in_configuration_documentation_for_underscores(self):
        self.maxDiff = None
        lExpected = []
        lActual = []
        for sFilename in glob.glob(os.path.join("docs", "configuring_*.rst")):
            lFile = []
            utils.read_file(sFilename, lFile)
            for sLine in lFile:
                if "html#" in sLine:
                    iStartIndex = sLine.index("html#") + 5
                    iEndIndex = sLine.index(">", iStartIndex)
                    sLink = sLine[iStartIndex:iEndIndex]
                    if "_" in sLink:
                        lActual.append(f"{sFilename}::{sLink}")

        self.assertEqual(lExpected, lActual)

    def test_rule_group_links(self):
        self.maxDiff = None
        oVhdlFile = vhdlFile.vhdlFile([""])
        oRuleList = rule_list.rule_list(oVhdlFile, None, None)

        dConfigurationFiles = {}
        for oRule in oRuleList.rules:
            for sGroup in oRule.groups:
                dConfigurationFiles[sGroup] = []

        for oRule in oRuleList.rules:
            for sGroup in oRule.groups:
                dConfigurationFiles[sGroup].append(oRule.unique_id)

        for sKey in list(dConfigurationFiles.keys()):
            sFileName = sKey.replace("::", "_") + "_rule_group.rst"
            sFullPathFileName = os.path.join("docs", "rule_groups", sFileName)
            lFile = []
            utils.read_file(sFullPathFileName, lFile)
            lActual = []
            bStartProcessing = False
            for sLine in lFile:
                if bStartProcessing:
                    if sLine.startswith("*"):
                        lLine = sLine.split()
                        lActual.append(lLine[1][1:])
                if sLine.startswith("Rules Enforcing"):
                    bStartProcessing = True
            self.assertEqual(dConfigurationFiles[sKey], lActual)

    def test_configuring_disabled_rules_doc(self):
        self.maxDiff = None
        oVhdlFile = vhdlFile.vhdlFile([""])
        oRuleList = rule_list.rule_list(oVhdlFile, None, None)

        lExpected = []
        for oRule in oRuleList.rules:
            if oRule.disable and not oRule.deprecated:
                lExpected.append(oRule.unique_id)

        sFileName = "configuring_disabled_rules.rst"
        sFullPathFileName = os.path.join("docs", sFileName)
        lFile = []
        utils.read_file(sFullPathFileName, lFile)
        lActual = []
        for sLine in lFile:
            if sLine.startswith("*"):
                lLine = sLine.split()
                lActual.append(lLine[1][1:])
        self.assertEqual(lExpected, lActual)

    def test_unfixable_rules_doc(self):
        self.maxDiff = None
        oVhdlFile = vhdlFile.vhdlFile([""])
        oRuleList = rule_list.rule_list(oVhdlFile, None, None)

        lExpected = []
        for oRule in oRuleList.rules:
            if not oRule.fixable and not oRule.proposed and not oRule.deprecated:
                lExpected.append(oRule.unique_id)

        sFileName = "unfixable_rules.rst"
        sFullPathFileName = os.path.join("docs", sFileName)
        lFile = []
        utils.read_file(sFullPathFileName, lFile)
        lActual = []
        for sLine in lFile:
            if sLine.startswith("*"):
                lLine = sLine.split()
                lActual.append(lLine[1][1:])

        for sExpected in lExpected:
            self.assertTrue(sExpected in lActual)

        for sActual in lActual:
            self.assertTrue(sActual in lExpected)

    def test_alias_declaration_rules_doc(self):
        lExpected, lActual = self.compare_files("alias_declaration")

        self.assertEqual(lExpected, lActual)

    def test_after_rules_doc(self):
        lExpected, lActual = self.compare_files("after")

        self.assertEqual(lExpected, lActual)

    def test_architecture_rules_doc(self):
        lExpected, lActual = self.compare_files("architecture")

        self.assertEqual(lExpected, lActual)

    def test_assert_rules_doc(self):
        lExpected, lActual = self.compare_files("assert")

        self.assertEqual(lExpected, lActual)

    def test_attribute_rules_doc(self):
        lExpected, lActual = self.compare_files("attribute")

        self.assertEqual(lExpected, lActual)

    def test_attribute_declaration_rules_doc(self):
        lExpected, lActual = self.compare_files("attribute_declaration")

        self.assertEqual(lExpected, lActual)

    def test_attribute_specification_rules_doc(self):
        lExpected, lActual = self.compare_files("attribute_specification")

        self.assertEqual(lExpected, lActual)

    def test_bit_string_literal_rules_doc(self):
        lExpected, lActual = self.compare_files("bit_string_literal")

        self.assertEqual(lExpected, lActual)

    def test_block_rules_doc(self):
        lExpected, lActual = self.compare_files("block")

        self.assertEqual(lExpected, lActual)

    def test_block_comment_rules_doc(self):
        lExpected, lActual = self.compare_files("block_comment")

        self.assertEqual(lExpected, lActual)

    def test_case_rules_doc(self):
        lExpected, lActual = self.compare_files("case")

        self.assertEqual(lExpected, lActual)

    def test_case_generate_alternative_rules_doc(self):
        lExpected, lActual = self.compare_files("case_generate_alternative")

        self.assertEqual(lExpected, lActual)

    def test_case_generate_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("case_generate_statement")

        self.assertEqual(lExpected, lActual)

    def test_if_generate_statements_rules_doc(self):
        lExpected, lActual = self.compare_files("if_generate_statement")

        self.assertEqual(lExpected, lActual)

    def test_comment_rules_doc(self):
        lExpected, lActual = self.compare_files("comment")

        self.assertEqual(lExpected, lActual)

    def test_component_rules_doc(self):
        lExpected, lActual = self.compare_files("component")

        self.assertEqual(lExpected, lActual)

    def test_concurrent_rules_doc(self):
        lExpected, lActual = self.compare_files("concurrent")

        self.assertEqual(lExpected, lActual)

    def test_conditional_expressions_rules_doc(self):
        lExpected, lActual = self.compare_files("conditional_expressions")

        self.assertEqual(lExpected, lActual)

    def test_conditional_waveforms_rules_doc(self):
        lExpected, lActual = self.compare_files("conditional_waveforms")

        self.assertEqual(lExpected, lActual)

    def test_constant_rules_doc(self):
        lExpected, lActual = self.compare_files("constant")

        self.assertEqual(lExpected, lActual)

    def test_context_rules_doc(self):
        lExpected, lActual = self.compare_files("context")

        self.assertEqual(lExpected, lActual)

    def test_context_ref_rules_doc(self):
        lExpected, lActual = self.compare_files("context_ref")

        self.assertEqual(lExpected, lActual)

    def test_element_association_rules_doc(self):
        lExpected, lActual = self.compare_files("element_association")

        self.assertEqual(lExpected, lActual)

    def test_entity_ref_rules_doc(self):
        lExpected, lActual = self.compare_files("entity")

        self.assertEqual(lExpected, lActual)

    def test_entity_specification_rules_doc(self):
        lExpected, lActual = self.compare_files("entity_specification")

        self.assertEqual(lExpected, lActual)

    def test_exit_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("exit_statement")

        self.assertEqual(lExpected, lActual)

    def test_exponent_rules_doc(self):
        lExpected, lActual = self.compare_files("exponent")

        self.assertEqual(lExpected, lActual)

    def test_external_constant_name_rules_doc(self):
        lExpected, lActual = self.compare_files("external_constant_name")

        self.assertEqual(lExpected, lActual)

    def test_external_signal_name_rules_doc(self):
        lExpected, lActual = self.compare_files("external_signal_name")

        self.assertEqual(lExpected, lActual)

    def test_external_variable_name_rules_doc(self):
        lExpected, lActual = self.compare_files("external_variable_name")

        self.assertEqual(lExpected, lActual)

    def test_file_rules_doc(self):
        lExpected, lActual = self.compare_files("file")

        self.assertEqual(lExpected, lActual)

    def test_for_loop_rules_doc(self):
        lExpected, lActual = self.compare_files("for_loop")

        self.assertEqual(lExpected, lActual)

    def test_function_rules_doc(self):
        lExpected, lActual = self.compare_files("function")

        self.assertEqual(lExpected, lActual)

    def test_generate_rules_doc(self):
        lExpected, lActual = self.compare_files("generate")

        self.assertEqual(lExpected, lActual)

    def test_generic_rules_doc(self):
        lExpected, lActual = self.compare_files("generic")

        self.assertEqual(lExpected, lActual)

    def test_generic_map_rules_doc(self):
        lExpected, lActual = self.compare_files("generic_map")

        self.assertEqual(lExpected, lActual)

    def test_if_rules_doc(self):
        lExpected, lActual = self.compare_files("if")

        self.assertEqual(lExpected, lActual)

    def test_instantiation_rules_doc(self):
        lExpected, lActual = self.compare_files("instantiation")

        self.assertEqual(lExpected, lActual)

    def test_interface_incomplete_type_declaration_rules_doc(self):
        lExpected, lActual = self.compare_files("interface_incomplete_type_declaration")

        self.assertEqual(lExpected, lActual)

    def test_iteration_scheme_doc(self):
        lExpected, lActual = self.compare_files("iteration_scheme")

        self.assertEqual(lExpected, lActual)

    def test_length_rules_doc(self):
        lExpected, lActual = self.compare_files("length")

        self.assertEqual(lExpected, lActual)

    def test_library_rules_doc(self):
        lExpected, lActual = self.compare_files("library")

        self.assertEqual(lExpected, lActual)

    def test_logical_operator_rules_doc(self):
        lExpected, lActual = self.compare_files("logical_operator")

        self.assertEqual(lExpected, lActual)

    def test_loop_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("loop_statement")

        self.assertEqual(lExpected, lActual)

    def test_package_rules_doc(self):
        lExpected, lActual = self.compare_files("package")

        self.assertEqual(lExpected, lActual)

    def test_package_body_rules_doc(self):
        lExpected, lActual = self.compare_files("package_body")

        self.assertEqual(lExpected, lActual)

    def test_port_rules_doc(self):
        lExpected, lActual = self.compare_files("port")

        self.assertEqual(lExpected, lActual)

    def test_port_map_rules_doc(self):
        lExpected, lActual = self.compare_files("port_map")

        self.assertEqual(lExpected, lActual)

    def test_pragma_rules_doc(self):
        lExpected, lActual = self.compare_files("pragma")

        self.assertEqual(lExpected, lActual)

    def test_procedure_rules_doc(self):
        lExpected, lActual = self.compare_files("procedure")

        self.assertEqual(lExpected, lActual)

    def test_procedure_call_rules_doc(self):
        lExpected, lActual = self.compare_files("procedure_call")

        self.assertEqual(lExpected, lActual)

    def test_process_rules_doc(self):
        lExpected, lActual = self.compare_files("process")

        self.assertEqual(lExpected, lActual)

    def test_range_rules_doc(self):
        lExpected, lActual = self.compare_files("range")

        self.assertEqual(lExpected, lActual)

    def test_record_type_definition_doc(self):
        lExpected, lActual = self.compare_files("record_type_definition")

        self.assertEqual(lExpected, lActual)

    def test_report_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("report_statement")

        self.assertEqual(lExpected, lActual)

    def test_return_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("return_statement")

        self.assertEqual(lExpected, lActual)

    def test_selected_assignment_rules_doc(self):
        lExpected, lActual = self.compare_files("selected_assignment")

        self.assertEqual(lExpected, lActual)

    def test_sequential_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("sequential")

        self.assertEqual(lExpected, lActual)

    def test_signal_statement_rules_doc(self):
        lExpected, lActual = self.compare_files("signal")

        self.assertEqual(lExpected, lActual)

    def test_source_file_rules_doc(self):
        lExpected, lActual = self.compare_files("source_file")

        self.assertEqual(lExpected, lActual)

    def test_subprogram_body_rules_doc(self):
        lExpected, lActual = self.compare_files("subprogram_body")

        self.assertEqual(lExpected, lActual)

    def test_subtype_rules_doc(self):
        lExpected, lActual = self.compare_files("subtype")

        self.assertEqual(lExpected, lActual)

    def test_type_rules_doc(self):
        lExpected, lActual = self.compare_files("type")

        self.assertEqual(lExpected, lActual)

    def test_use_clause_rules_doc(self):
        lExpected, lActual = self.compare_files("use_clause")

        self.assertEqual(lExpected, lActual)

    def test_variable_rules_doc(self):
        lExpected, lActual = self.compare_files("variable")

        self.assertEqual(lExpected, lActual)

    def test_variable_assignment_rules_doc(self):
        lExpected, lActual = self.compare_files("variable_assignment")

        self.assertEqual(lExpected, lActual)

    def test_wait_rules_doc(self):
        lExpected, lActual = self.compare_files("wait")

        self.assertEqual(lExpected, lActual)

    def test_when_rules_doc(self):
        lExpected, lActual = self.compare_files("when")

        self.assertEqual(lExpected, lActual)

    def test_while_loop_rules_doc(self):
        lExpected, lActual = self.compare_files("while_loop")

        self.assertEqual(lExpected, lActual)

    def test_whitespace_rules_doc(self):
        lExpected, lActual = self.compare_files("whitespace")

        self.assertEqual(lExpected, lActual)

    def test_with_rules_doc(self):
        lExpected, lActual = self.compare_files("with")

        self.assertEqual(lExpected, lActual)
