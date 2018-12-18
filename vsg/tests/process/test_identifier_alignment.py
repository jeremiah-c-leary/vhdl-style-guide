
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile

#from vsg.tests import utils

class test_process_rules(unittest.TestCase):

    def setUp(self):
        self.sFile = os.path.join(os.path.dirname(__file__),'identifier_alignment_input.vhd')
        self.oFile = vhdlFile.vhdlFile(self.sFile)

    def test_031(self):
        oRule = process.rule_031()
        oRule.analyze(self.oFile)
        lExpected = ['22-32', '36-46']
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_031(self):
        oRule = process.rule_031()
        dExpected = []
        oRule.fix(self.oFile)
#        utils.debug_lines(self.oFile, 22, 11)
        self.assertEqual(self.oFile.lines[4].line, '  variable var1 : boolean := False;')
        self.assertEqual(self.oFile.lines[5].line, '  constant con1 : integer;')
        self.assertEqual(self.oFile.lines[6].line, '  signal sig1 : std_logic; -- Sig')
        self.assertEqual(self.oFile.lines[7].line, '  file file1 : load_file_file open read_mode is load_file_name;')
        self.assertEqual(self.oFile.lines[24].line, '    variable var1   : boolean;')
        self.assertEqual(self.oFile.lines[25].line, '    constant con1   : integer := 1;')
        self.assertEqual(self.oFile.lines[26].line, '    file     file1  : load_file_file open read_mode is load_file_name; -- 1')
        self.assertEqual(self.oFile.lines[27].line, '')
        self.assertEqual(self.oFile.lines[28].line, '    variable var12  : boolean;')
        self.assertEqual(self.oFile.lines[29].line, '    constant con12  : integer;')
        self.assertEqual(self.oFile.lines[30].line, '    file     file12 : load_file_file open read_mode is load_file_name; -- 2')

        self.assertEqual(self.oFile.lines[38].line, '    variable var1   : boolean;')
        self.assertEqual(self.oFile.lines[39].line, '    constant con1   : integer;')
        self.assertEqual(self.oFile.lines[40].line, '    file     file1  : load_file_file open read_mode is load_file_name; -- 3')
        self.assertEqual(self.oFile.lines[41].line, '')
        self.assertEqual(self.oFile.lines[42].line, '    variable var12  : boolean;')
        self.assertEqual(self.oFile.lines[43].line, '    constant con12  : integer;')
        self.assertEqual(self.oFile.lines[44].line, '    file     file12 : load_file_file open read_mode is load_file_name; -- 4')
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
