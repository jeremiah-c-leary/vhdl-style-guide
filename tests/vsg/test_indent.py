# -*- coding: utf-8 -*-
import contextlib
import filecmp
import os
import pathlib
import shutil
import subprocess
import sys
import unittest
from io import StringIO
from tempfile import TemporaryDirectory
from unittest import mock

import yaml

from tests import utils
from vsg import __main__, version


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version
        self.style = "indent_only"
        self.configuration = []
        self.debug = False
        self.fix_only = False
        self.stdin = False
        self.force_fix = False
        self.fix = False


class testMain(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    @mock.patch("sys.stdout")
    def test_invalid_group(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call("ERROR: Invalid indent configuration detected"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following group does not exist:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    tokens:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        simple_something:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following groups are available:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    tokens:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        alias_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        architecture_body:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        assertion:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        assertion_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        association_element:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        attribute_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        attribute_specification:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        block_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        case_generate_alternative:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        case_generate_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        case_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        case_statement_alternative:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        component_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        component_instantiation_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        concurrent_assertion_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        concurrent_conditional_signal_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        concurrent_procedure_call_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        concurrent_selected_signal_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        concurrent_signal_assignment_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        concurrent_simple_signal_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        conditional_waveform_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        conditional_variable_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        context_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        constant_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        if_generate_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        entity_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        enumeration_type_definition:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        exit_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        file_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        file_open_information:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        for_generate_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        full_type_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        function_specification:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        generate_statement_body:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        generic_clause:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        generic_map_aspect:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        identifier_list:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        if_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        incomplete_type_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_constant_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_file_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_function_specification:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_incomplete_type_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_package_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_procedure_specification:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_signal_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_unknown_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        interface_variable_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        iteration_scheme:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        library_clause:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        loop_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        next_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        null_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        package_body:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        package_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        package_instantiation_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        port_clause:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        port_map_aspect:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        procedure_call:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        procedure_call_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        procedure_specification:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        process_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        protected_type_body:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        protected_type_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        record_type_definition:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        report_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        return_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        selected_force_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        selected_variable_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        selected_waveform_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        signal_assignment_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        signal_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        simple_force_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        simple_release_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        simple_variable_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        simple_waveform_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        subprogram_body:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        subprogram_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        subprogram_instantiation_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        subtype_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        use_clause:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        variable_assignment_statement:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        variable_declaration:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("        wait_statement:"))
        lExpected.append(mock.call("\n"))

        sys.argv = ["vsg"]
        sys.argv.extend(["--configuration", "tests/vsg/indent/config_group.yaml"])
        sys.argv.extend(["-p 1"])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch("sys.stdout")
    def test_invalid_token(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call("ERROR: Invalid indent configuration detected"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following token does not exist:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    tokens:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        simple_variable_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            target:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following tokens are available:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    tokens:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        simple_variable_assignment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            simple_name:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            aggregate_open_parenthesis:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            aggregate_close_parenthesis:"))
        lExpected.append(mock.call("\n"))

        sys.argv = ["vsg"]
        sys.argv.extend(["--configuration", "tests/vsg/indent/config_token.yaml"])
        sys.argv.extend(["-p 1"])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch("sys.stdout")
    def test_invalid_option(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call("ERROR: Invalid indent option detected"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following option does not exist:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    options:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        blah:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following options are available:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    options:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        comment:"))
        lExpected.append(mock.call("\n"))

        sys.argv = ["vsg"]
        sys.argv.extend(["--configuration", "tests/vsg/indent/config_option.yaml"])
        sys.argv.extend(["-p 1"])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch("sys.stdout")
    def test_invalid_option_parameter(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call("ERROR: Invalid indent option parameter detected"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following option parameter does not exist:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    options:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        comment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            blah:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("The following option parameters are available:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(""))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("indent:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call("    options:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"        comment:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            align_with_end_of_declarative_part:"))
        lExpected.append(mock.call("\n"))
        lExpected.append(mock.call(f"            align_with_end_of_statement_part:"))
        lExpected.append(mock.call("\n"))

        sys.argv = ["vsg"]
        sys.argv.extend(["--configuration", "tests/vsg/indent/config_option_parameter.yaml"])
        sys.argv.extend(["-p 1"])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)
