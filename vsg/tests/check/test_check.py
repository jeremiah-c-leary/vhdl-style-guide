import os
import unittest

from vsg import rule
from vsg import check
from vsg import line
from vsg import vhdlFile

sFileName = os.path.join(os.path.dirname(__file__),'check_test_input.txt')


class testCheckFunctions(unittest.TestCase):

    def test_is_no_blank_line_after(self):
        oFile = vhdlFile.vhdlFile(sFileName)
        oFile.lines.append(line.line('Simple line'))
        oFile.lines.append(line.blank_line())

        oRule = no_blank_check_rule()
        self.assertEqual(oRule.violations, [])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [1])

    def test_get_package_name(self):
        self.assertEqual(check.get_package_name(line.line('end package FIFO;')), 'FIFO')
        self.assertEqual(check.get_package_name(line.line('end package;')), '')
        self.assertEqual(check.get_package_name(line.line('end FIFO;')), '')
        self.assertEqual(check.get_package_name(line.line('end;')), '')
        self.assertEqual(check.get_package_name(line.line('package FIFO_PKG is')), 'FIFO_PKG')


class no_blank_check_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self, 'debug', '001')
        self.solution = None
        self.phase = None

    def analyze(self, oFile):
        check.is_no_blank_line_after(self, oFile, 1)
