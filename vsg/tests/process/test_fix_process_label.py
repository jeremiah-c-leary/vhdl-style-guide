
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils


sFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'process_label_test_input.vhd'))

class test_fix(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(sFile)

    def test_rule_032(self):
        oRule = process.rule_032()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '032')
        dExpected = [16, 25]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_032(self):
        oRule = process.rule_032()
        oRule.fix(self.oFile)
##        utils.debug_lines(self.oFile, 22, 11)


        self.assertEqual(self.oFile.lines[15].line, '')
        self.assertTrue(self.oFile.lines[15].isBlank)
        self.assertEqual(self.oFile.lines[16].line, 'LABEL1 :   process (A) is')
        self.assertTrue(self.oFile.lines[16].isProcessLabel)

        self.assertEqual(self.oFile.lines[23].line, '')
        self.assertTrue(self.oFile.lines[23].isBlank)
        self.assertEqual(self.oFile.lines[24].line, '')
        self.assertEqual(self.oFile.lines[25].line, 'LABEL1 :   process (A) is')
        self.assertTrue(self.oFile.lines[25].isProcessLabel)

        dExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
