# -*- coding: utf-8 -*-
import subprocess
import unittest


class command_line_args:
    """This is used as an input into the version command."""

    def __init__(self, version=False):
        self.version = version


class testVsg(unittest.TestCase):
    def test_rc_command_line_argument_w_invalid_rule(self):
        lExpected = []
        lExpected.append("ERROR: rule unknown_rule_001 was not found.")
        lExpected.append("")
        iExitStatus = -1

        try:
            subprocess.check_output(["bin/vsg", "-rc", "unknown_rule_001"])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode("utf-8")).split("\n")
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(lActual, lExpected)
