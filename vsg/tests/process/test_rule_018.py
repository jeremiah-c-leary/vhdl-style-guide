import os

import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_rule_018_test_input.vhd'))

class test_rule_018(unittest.TestCase):

  def setUp(self):
    self.oFile = vhdlFile.vhdlFile(lFile)


  def test_rule_018(self):
    oRule = process.rule_018()
    self.assertTrue(oRule)
    self.assertEqual(oRule.name, 'process')
    self.assertEqual(oRule.identifier, '018')
    oRule.analyze(self.oFile)
    dExpected = [{'lineNumber': 14, 'processLabel': 'PROC_LABEL2'}, {'lineNumber': 19}]
    self.assertEqual(oRule.violations, dExpected)

  def test_fix_rule_018(self):
    oRule = process.rule_018()
    oRule.fix(self.oFile)

    self.assertEqual(self.oFile.lines[9].line, '  end process PROC_LABEL1;')
    self.assertEqual(self.oFile.lines[14].line, '  end process PROC_LABEL2;')
    self.assertEqual(self.oFile.lines[19].line, '  end process;')
    self.assertEqual(self.oFile.lines[24].line, '  end process PROC_LABEL3;')
    oRule.analyze(self.oFile)
    dExpected = [{'lineNumber': 19}]
    self.assertEqual(oRule.violations, dExpected)
