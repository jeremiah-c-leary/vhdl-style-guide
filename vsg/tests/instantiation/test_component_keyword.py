import os

import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils



class testComponentKeyword(unittest.TestCase):

    def setUp(self):
        self.lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_component_keyword_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(self.lFile)

    def test_rule_031(self):
        oRule = instantiation.rule_031()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '031')
        self.assertTrue(oRule.disable)

        dExpected = [{'line_number': 13, 'words_to_fix': {'COMPONENT'}},
                     {'line_number': 20, 'words_to_fix': {'Component'}}]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_031(self):
        oRule = instantiation.rule_031()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[6].line,  '  U_INST1 : component INST1')
        self.assertEqual(self.oFile.lines[13].line, '  U_INST1 : component INST1')
        self.assertEqual(self.oFile.lines[20].line, '  U_INST1 :component INST1')
        self.assertEqual(self.oFile.lines[27].line, '  U_INST1 : INST1')

        self.assertEqual(oRule.violations, [])

    def test_rule_032(self):
        oRule = instantiation.rule_032()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '032')
        self.assertTrue(oRule.disable)

        dExpected = [41, 48]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_032(self):
        oRule = instantiation.rule_032()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[34].line, '  U_INST1 : component INST1')
        self.assertEqual(self.oFile.lines[41].line, '  U_INST1 : component INST1')
        self.assertEqual(self.oFile.lines[48].line, '  U_INST1 : component INST1')

        self.assertEqual(oRule.violations, [])

    def test_rule_033(self):
        oRule = instantiation.rule_033()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '033')
        self.assertFalse(oRule.disable)

        dExpected = [6,13,20,34,41,48]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_033(self):
        oRule = instantiation.rule_033()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[6].line, '  U_INST1 : INST1')
        self.assertEqual(self.oFile.lines[13].line, '  U_INST1 : INST1')
        self.assertEqual(self.oFile.lines[20].line, '  U_INST1 : INST1')
        self.assertEqual(self.oFile.lines[27].line, '  U_INST1 : INST1')
        self.assertEqual(self.oFile.lines[34].line, '  U_INST1 : INST1')
        self.assertEqual(self.oFile.lines[41].line, '  U_INST1 : INST1')
        self.assertEqual(self.oFile.lines[48].line, '  U_INST1 : INST1')

        self.assertEqual(oRule.violations, [])
