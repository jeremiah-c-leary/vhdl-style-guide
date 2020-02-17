import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentCase(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_002(self):
        oRule = subtype.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [{'lineNumber': 7, 'subtype': 'READ_SIZE'},
                     {'lineNumber': 11, 'subtype': 'WRITE_size'}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oRule._get_solution(7), 'Inconsistent capitalization of word: READ_SIZE')
        self.assertEqual(oRule._get_solution(11), 'Inconsistent capitalization of word: WRITE_size')

    def test_fix_rule_002(self):
        oRule = subtype.rule_002()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[7].line, '  signal read  : read_size;')
        self.assertEqual(self.oFile.lines[11].line, '  constant write_sz : write_size := 1;')
        self.assertEqual(oRule.violations, [])
