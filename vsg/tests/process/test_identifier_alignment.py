
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils


class test_process_rules(unittest.TestCase):

    def setUp(self):
        self.sFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'identifier_alignment_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(self.sFile)

    def test_031(self):
        oRule = process.rule_031()
        oRule.analyze(self.oFile)
        lExpected = ['19-28']
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_031(self):
        oRule = process.rule_031()
        dExpected = []
        oRule.fix(self.oFile)
#        utils.debug_lines(self.oFile, 22, 11)
        self.assertEqual(self.oFile.lines[4].line, '  constant con1 : integer;')
        self.assertEqual(self.oFile.lines[5].line, '  signal sig1 : std_logic; -- Sig')
        self.assertEqual(self.oFile.lines[6].line, '  file file1 : load_file_file open read_mode is load_file_name;')
        self.assertEqual(self.oFile.lines[21].line, '    variable var1 : boolean;')
        self.assertEqual(self.oFile.lines[22].line, '    constant con1 : integer := 1;')
        self.assertEqual(self.oFile.lines[23].line, '    file     file1 : load_file_file open read_mode is load_file_name; -- 1')
        self.assertEqual(self.oFile.lines[27].line, '')
        self.assertEqual(self.oFile.lines[24].line, '    variable var12 : boolean;')
        self.assertEqual(self.oFile.lines[25].line, '    constant con12 : integer;')
        self.assertEqual(self.oFile.lines[26].line, '    file     file12 : load_file_file open read_mode is load_file_name; -- 2')

        self.assertEqual(self.oFile.lines[34].line, '    variable var1 : boolean;')
        self.assertEqual(self.oFile.lines[35].line, '    constant con1 : integer;')
        self.assertEqual(self.oFile.lines[36].line, '    file     file1 : load_file_file open read_mode is load_file_name; -- 3')
        self.assertEqual(self.oFile.lines[37].line, '')
        self.assertEqual(self.oFile.lines[38].line, '    variable var12 : boolean;')
        self.assertEqual(self.oFile.lines[39].line, '    constant con12 : integer;')
        self.assertEqual(self.oFile.lines[40].line, '    file     file12 : load_file_file open read_mode is load_file_name; -- 4')
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
