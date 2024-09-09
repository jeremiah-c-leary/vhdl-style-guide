# -*- coding: utf-8 -*-
import os
import sys
import unittest
from tempfile import TemporaryDirectory
from unittest import mock

from vsg import __rule_doc_gen__


class testMain(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()

    def tearDown(self):
        self._tmpdir.cleanup()

    @mock.patch("sys.stdout")
    def test_w_user_provided_path(self, mock_stdout):
        lExpected = []

        sys.argv = ["vsg_rule_doc_gen"]
        sys.argv.extend(["-p", self._tmpdir.name])

        try:
            __rule_doc_gen__.main()
        except SystemExit:
            pass

        # Check that the temporary directory is not empty after document
        # generation. Detailed checking is left to test_rule_doc.
        self.assertNotEqual([], os.listdir(self._tmpdir.name))

        mock_stdout.write.assert_has_calls(lExpected)
