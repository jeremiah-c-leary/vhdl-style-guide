# -*- coding: utf-8 -*-
import io
import os
import pathlib
import subprocess
import sys
import unittest
from tempfile import TemporaryDirectory
from unittest import mock

from tests import utils
from vsg import version


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version


class testVsg(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_multiple_configuration_w_multiple_filelists(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "--configuration", "tests/vsg/config_1.json", "tests/vsg/config_2.json", "--output_format", "syntastic"],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_single_configuration_w_filelist(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_1.json", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_2.json", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_single_configuration_w_rule_disable(self):
        lExpected = []

        lActual = subprocess.check_output(
            [*utils.vsg_exec(), "--configuration", "tests/vsg/config_3.json", "--output_format", "syntastic", "-f", "tests/vsg/entity1.vhd"],
        )
        lActual = str(lActual.decode("utf-8")).splitlines()
        self.assertEqual(lActual, lExpected)

    def test_multiple_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")

        try:
            subprocess.check_output(
                [
                    *utils.vsg_exec(),
                    "--configuration",
                    "tests/vsg/config_3.json",
                    "tests/vsg/config_4.json",
                    "--output_format",
                    "syntastic",
                    "-f",
                    "tests/vsg/entity1.vhd",
                ],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_reverse_multiple_configuration_w_rule_disable(self):
        lExpected = []

        lActual = subprocess.check_output(
            [
                *utils.vsg_exec(),
                "--configuration",
                "tests/vsg/config_4.json",
                "tests/vsg/config_3.json",
                "--output_format",
                "syntastic",
                "-f",
                "tests/vsg/entity1.vhd",
            ],
        )
        lActual = str(lActual.decode("utf-8")).splitlines()
        self.assertEqual(lActual, lExpected)

    def test_invalid_configuration(self):
        lExpected = []
        lExpected.append("ERROR: Invalid configuration file: tests/vsg/config_error.json")
        lExpected.append("while parsing a flow node")
        lExpected.append("expected the node content, but found ','")
        lExpected.append('  in "tests/vsg/config_error.json", line 2, column 16')
        config_error_file = os.path.join(self._tmpdir.name, "config_error.actual.xml")
        try:
            lActual = subprocess.check_output(
                [
                    *utils.vsg_exec(),
                    "--configuration",
                    "tests/vsg/config_error.json",
                    "--output_format",
                    "syntastic",
                    "-f",
                    "tests/vsg/entity1.vhd",
                    "--junit",
                    config_error_file,
                ],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)
        self.assertEqual(iExitStatus, 1)

        # Read in the expected JUnit XML file for comparison
        lExpected = []
        utils.read_file(os.path.join(os.path.dirname(__file__), "config_error.expected.xml"), lExpected)
        # Read in the actual JUnit XML file for comparison
        lActual = []
        utils.read_file(config_error_file, lActual)
        # Compare the two files, but skip the line with the timestamp (as it will never match)
        for iLineNumber, sLine in enumerate(lExpected):
            if iLineNumber != 1:
                self.assertEqual(sLine, lActual[iLineNumber])

    def test_local_rules(self):
        lExpected = ["ERROR: tests/vsg/entity_architecture.vhd(1)localized_001 -- Split entity and architecture into separate files."]

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "--style", "jcl", "-f", "tests/vsg/entity_architecture.vhd", "-of", "syntastic", "-lr", "tests/vsg/local_rules"],
            )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_invalid_local_rule_directory(self):
        lExpected = [
            "ERROR: encountered FileNotFoundError, No such file or directory tests/vsg/invalid_local_rule_directory when trying to open local rules file.",
        ]

        try:
            lActual = subprocess.check_output(
                [*utils.vsg_exec(), "-f", "tests/vsg/entity_architecture.vhd", "-of", "syntastic", "-lr", "tests/vsg/invalid_local_rule_directory"],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(lActual, lExpected)

    def test_globbing_filenames_in_configuration(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_glob.json", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)
        if lActual[0] == lExpected[1]:
            lExpected = []
            lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")
            lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        self.assertEqual(lActual, lExpected)

    def test_single_yaml_configuration_w_filelist(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_1.yaml", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_2.json", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_multiple_yaml_configuration_w_multiple_filelists(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "--configuration", "tests/vsg/config_1.yaml", "tests/vsg/config_2.yaml", "--output_format", "syntastic"],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_single_yaml_configuration_w_rule_disable(self):
        lExpected = []

        lActual = subprocess.check_output(
            [*utils.vsg_exec(), "--configuration", "tests/vsg/config_3.yaml", "--output_format", "syntastic", "-f", "tests/vsg/entity1.vhd"],
        )
        lActual = str(lActual.decode("utf-8")).splitlines()
        self.assertEqual(lActual, lExpected)

    def test_multiple_yaml_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")

        try:
            subprocess.check_output(
                [
                    *utils.vsg_exec(),
                    "--configuration",
                    "tests/vsg/config_3.yaml",
                    "tests/vsg/config_4.yaml",
                    "--output_format",
                    "syntastic",
                    "-f",
                    "tests/vsg/entity1.vhd",
                ],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_reverse_yaml_multiple_configuration_w_rule_disable(self):
        lExpected = []

        lActual = subprocess.check_output(
            [
                *utils.vsg_exec(),
                "--configuration",
                "tests/vsg/config_4.yaml",
                "tests/vsg/config_3.yaml",
                "--output_format",
                "syntastic",
                "-f",
                "tests/vsg/entity1.vhd",
            ],
        )
        lActual = str(lActual.decode("utf-8")).splitlines()
        self.assertEqual(lActual, lExpected)

    def test_globbing_filenames_in_yaml_configuration(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")
        lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_glob.yaml", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        if lActual[0] == lExpected[1]:
            lExpected = []
            lExpected.append("ERROR: tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.")
            lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        self.assertEqual(lActual, lExpected)

    def test_oc_command_line_argument(self):
        lExpected = []

        lActual = subprocess.check_output([*utils.vsg_exec(), "-oc", os.path.join(self._tmpdir.name, "deleteme.json")])
        lActual = str(lActual.decode("utf-8")).splitlines()
        self.assertEqual(lActual, lExpected)

    def test_missing_configuration_file(self):
        try:
            subprocess.check_output([*utils.vsg_exec(), "-c", "missing_configuration.yaml"], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

    @unittest.skipIf(utils.is_user_admin(), "We are root. Root always has permissions so test will fail.")
    @unittest.skipIf(utils.is_windows(), "Permission based tests can not be run on Windows.")
    def test_no_permission_configuration_file(self):
        sNoPermissionFile = os.path.join(self._tmpdir.name, "no_permission.yml")
        pathlib.Path(sNoPermissionFile).touch(mode=0o222, exist_ok=True)

        sExpected = f"ERROR: encountered PermissionError, Permission denied while opening configuration file: {sNoPermissionFile}\n"

        try:
            subprocess.check_output([*utils.vsg_exec(), "-c", sNoPermissionFile])
        except subprocess.CalledProcessError as e:
            sActual = str(e.output.decode("utf-8"))
            iExitStatus = e.returncode

            self.assertEqual(iExitStatus, 1)

            self.assertEqual(sActual, sExpected)

    def test_missing_files_in_configuration_file(self):
        lExpected = []
        lExpected.append("ERROR: Could not find file missing_file.vhd in configuration file tests/vsg/missing_file_config.yaml")

        try:
            subprocess.check_output([*utils.vsg_exec(), "-c", "tests/vsg/missing_file_config.yaml", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)

    def test_summary_output_format_error(self):
        lExpectedStdErr = ["File: tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]"]
        lExpectedStdOut = []

        try:
            subprocess.check_output([*utils.vsg_exec(), "-f", "tests/vsg/entity_architecture.vhd", "-of", "summary"], stderr=subprocess.PIPE)
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode("utf-8")).splitlines()
            lActualStdErr = str(e.stderr.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_error_with_local_rules(self):
        lExpectedStdErr = ["File: tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]"]
        lExpectedStdOut = []

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "-f", "tests/vsg/entity_architecture.vhd", "-of", "summary", "-lr", "tests/vsg/local_rules"],
                stderr=subprocess.PIPE,
            )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode("utf-8")).splitlines()
            lActualStdErr = str(e.stderr.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_ok(self):
        lExpected = ["File: tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]"]

        lActual = (
            subprocess.check_output([*utils.vsg_exec(), "-f", "tests/vsg/entity_architecture.fixed.vhd", "-of", "summary"], stderr=subprocess.STDOUT)
            .decode("utf-8")
            .splitlines()
        )

        self.assertEqual(utils.replace_total_count_summary(lActual), lExpected)

    def test_summary_output_format_multiple_mixed(self):
        lExpectedStdErr = [
            "File: tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]",
            "File: tests/vsg/entity1.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]",
            "File: tests/vsg/entity2.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]",
        ]
        lExpectedStdOut = ["File: tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]"]

        try:
            subprocess.check_output(
                [
                    *utils.vsg_exec(),
                    "-f",
                    "tests/vsg/entity_architecture.vhd",
                    "tests/vsg/entity_architecture.fixed.vhd",
                    "tests/vsg/entity1.vhd",
                    "tests/vsg/entity2.vhd",
                    "--output_format",
                    "summary",
                ],
                stderr=subprocess.PIPE,
            )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode("utf-8")).splitlines()
            lActualStdErr = str(e.stderr.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_multiple_mixed_jobs_1(self):
        lExpectedStdErr = [
            "File: tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]",
            "File: tests/vsg/entity1.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]",
            "File: tests/vsg/entity2.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]",
        ]
        lExpectedStdOut = ["File: tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]"]

        try:
            subprocess.check_output(
                [
                    *utils.vsg_exec(),
                    "-f",
                    "tests/vsg/entity_architecture.vhd",
                    "tests/vsg/entity_architecture.fixed.vhd",
                    "tests/vsg/entity1.vhd",
                    "tests/vsg/entity2.vhd",
                    "--output_format",
                    "summary",
                    "--jobs=1",
                ],
                stderr=subprocess.PIPE,
            )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode("utf-8")).splitlines()
            lActualStdErr = str(e.stderr.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_multiple_mixed_jobs_2(self):
        lExpectedStdErr = [
            "File: tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]",
            "File: tests/vsg/entity1.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]",
            "File: tests/vsg/entity2.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]",
        ]
        lExpectedStdOut = ["File: tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]"]

        try:
            subprocess.check_output(
                [
                    *utils.vsg_exec(),
                    "-f",
                    "tests/vsg/entity_architecture.vhd",
                    "tests/vsg/entity_architecture.fixed.vhd",
                    "tests/vsg/entity1.vhd",
                    "tests/vsg/entity2.vhd",
                    "--output_format",
                    "summary",
                    "-p 2",
                ],
                stderr=subprocess.PIPE,
            )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode("utf-8")).splitlines()
            lActualStdErr = str(e.stderr.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_globbing_filenames_in_configuration_with_file_rules(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        try:
            subprocess.check_output([*utils.vsg_exec(), "--configuration", "tests/vsg/config_glob_with_file_rules.yaml", "--output_format", "syntastic"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)

    def test_configuration_with_file_rules_and_no_file_list_entity2(self):
        lExpected = []
        lExpected.append("ERROR: tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.")

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "--configuration", "tests/vsg/config_file_rules.yaml", "-f", "tests/vsg/entity2.vhd", "--output_format", "syntastic"],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)

    def test_configuration_with_file_rules_and_no_file_list_entity1(self):
        lExpected = []

        lActual = []

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "--configuration", "tests/vsg/config_file_rules.yaml", "-f", "tests/vsg/entity1.vhd", "--output_format", "syntastic"],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)

    def test_configuration_with_globbing_in_file_rules(self):
        lExpected = []

        lActual = []

        try:
            subprocess.check_output(
                [*utils.vsg_exec(), "--configuration", "tests/vsg/config_file_rules_w_globbing.yaml", "-f", "tests/vsg/*.vhd", "--output_format", "syntastic"],
            )
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).splitlines()
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)

    def test_file_as_stdin(self):
        with open("tests/vsg/entity1.vhd") as file1:
            lExpected = []

            lActual = subprocess.check_output(
                [*utils.vsg_exec(), "--configuration", "tests/vsg/config_3.yaml", "--output_format", "syntastic", "--stdin"],
                stdin=file1,
            )
            lActual = str(lActual.decode("utf-8")).splitlines()
            self.assertEqual(lActual, lExpected)
