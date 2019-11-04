import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'multi_line_signal_test_input.vhd'))

class testGeneralRule(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_015_consecutive_default(self):
        oRule = signal.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [5,8]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_consecutive_1(self):
        oRule = signal.rule_015()
        oRule.consecutive = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [5,8,40,42,45,49,54,60,67]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_fix_rule_014(self):
#        oRule = signal.rule_014()
#        oRule.fix(self.oFile)
#        oRule.analyze(self.oFile)
#
#        self.assertEqual(self.oFile.lines[22].line, '  PROC_NAME : process (sig2) is')
#        self.assertEqual(self.oFile.lines[25].line, '    sig1 <= \'0\';')
#        self.assertEqual(self.oFile.lines[27].line, '    if (sig2 = \'0\') then')
#        self.assertEqual(self.oFile.lines[28].line, '      sig1 <= \'1\';')
#        self.assertEqual(self.oFile.lines[29].line, '    elsif (sig2 = \'1\') then')
#        self.assertEqual(self.oFile.lines[30].line, '      sig1 <= \'0\';')
#        self.assertEqual(self.oFile.lines[38].line, '    SIG1 => sig1,')
#        self.assertEqual(self.oFile.lines[39].line, '    SIG2 => sig2,')
#        self.assertEqual(self.oFile.lines[40].line, '    SIG3 => sig3')
#        self.assertEqual(self.oFile.lines[46].line, '    SIG3 => sig3,')
#        self.assertEqual(self.oFile.lines[47].line, '    SIG4 => sig4,')
#        self.assertEqual(self.oFile.lines[48].line, '    SIG5 => sig5')
#        self.assertEqual(self.oFile.lines[54].line, '    SIG6 => sig6,')
#        self.assertEqual(self.oFile.lines[55].line, '    SIG7 => sig7')
#        self.assertEqual(self.oFile.lines[58].line, '  sig1 <= \'0\';')
#        self.assertEqual(self.oFile.lines[59].line, '  sig1 <= sig2 and sig3;')
#        self.assertEqual(self.oFile.lines[60].line, '  sig1 <= sig2 and sig3;')
#        self.assertEqual(self.oFile.lines[61].line, '  sig1 <= sig2 and')
#        self.assertEqual(self.oFile.lines[62].line, '          sig3;')
#        self.assertEqual(self.oFile.lines[63].line, '  sig1 <= sig2 and sig3;')
#        self.assertEqual(self.oFile.lines[64].line, '  sig1 <= sig1 or sig1;')
#
#        self.assertEqual(oRule.violations, [])
