# -*- coding: utf-8 -*-
import contextlib
import filecmp
import os
import pathlib
import sys
import unittest
from io import StringIO
from tempfile import TemporaryDirectory
from unittest import mock

from tests import utils
from vsg import __main__


class testMain(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    @mock.patch("sys.stdout")
    def test_multiple_configuration_w_multiple_filelists(self, mock_stdout):
        sExpected = "ERROR: tests/tool_integration/quality_report/example.vhd(4)entity_015 -- Add *entity* keyword"
        sExpected += "\n"
        sExpected += "ERROR: tests/tool_integration/quality_report/example.vhd(4)entity_019 -- Add entity simple name"
        sExpected += "\n"
        sExpected += "ERROR: tests/tool_integration/quality_report/example.vhd(8)architecture_010 -- Add architecture keyword."
        sExpected += "\n"
        sExpected += "ERROR: tests/tool_integration/quality_report/example.vhd(8)architecture_024 -- Add architecture simple name"
        lExpected = []
        lExpected.append(mock.call(sExpected))
        lExpected.append(mock.call("\n"))

        actual_file = os.path.join(self._tmpdir.name, "actual.json")

        sys.argv = ["vsg"]
        sys.argv.extend(["--output_format", "syntastic"])
        sys.argv.extend(["-f", "tests/tool_integration/quality_report/example.vhd"])
        sys.argv.extend(["-p 1"])
        sys.argv.extend(["--quality_report", actual_file])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertTrue(os.path.isfile(actual_file))

        lActual = []
        lActual = utils.read_file(actual_file, lActual)

        lExpected = []
        lExpected = utils.read_file(os.path.join("tests", "tool_integration", "quality_report", "expected.json"), lExpected)

        self.assertEqual(lExpected, lActual)
