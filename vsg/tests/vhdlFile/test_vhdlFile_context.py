import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','context','context_classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_context(unittest.TestCase):

    def test_context_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((7,0))
        lExpected.append((12,0))
        lExpected.append((21,0))
        lExpected.append((28,0))
        lExpected.append((37,0))
        lExpected.append((39,0))
        lExpected.append((41,0))
        lExpected.append((45,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_identifier(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((7,2))
        lExpected.append((13,0))
        lExpected.append((22,0))
        lExpected.append((29,0))
        lExpected.append((37,2))
        lExpected.append((39,2))
        lExpected.append((41,2))
        lExpected.append((46,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_is_keyword(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((8,0))
        lExpected.append((14,0))
        lExpected.append((23,0))
        lExpected.append((30,0))
        lExpected.append((37,4))
        lExpected.append((39,4))
        lExpected.append((41,4))
        lExpected.append((47,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_is_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_end_keyword(self):
        lExpected = []
        lExpected.append((4,0))
        lExpected.append((10,0))
        lExpected.append((16,0))
        lExpected.append((25,0))
        lExpected.append((32,0))
        lExpected.append((37,16))
        lExpected.append((39,16))
        lExpected.append((41,16))
        lExpected.append((49,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_end_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_end_context_keyword(self):
        lExpected = []
        lExpected.append((4,2))
        lExpected.append((10,2))
        lExpected.append((17,0))
        lExpected.append((33,0))
        lExpected.append((39,18))
        lExpected.append((41,18))
        lExpected.append((50,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_end_context_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_end_identifier(self):
        lExpected = []
        lExpected.append((4,4))
        lExpected.append((10,4))
        lExpected.append((18,0))
        lExpected.append((41,20))
        lExpected.append((51,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_end_identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_colon(self):
        lExpected = []
        lExpected.append((4,5))
        lExpected.append((10,5))
        lExpected.append((19,0))
        lExpected.append((26,0))
        lExpected.append((34,0))
        lExpected.append((37,17))
        lExpected.append((39,19))
        lExpected.append((41,21))
        lExpected.append((52,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_colon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_get_context_declarations(self):
        lActual = oFile.get_context_declarations()
        self.assertEqual(9, len(lActual))
        self.assertEqual(3, len(lActual[0]['lines']))
        self.assertEqual(4, len(lActual[1]['lines']))
        self.assertEqual(8, len(lActual[2]['lines']))
        self.assertEqual(6, len(lActual[3]['lines']))
        self.assertEqual(7, len(lActual[4]['lines']))
        self.assertEqual(28, lActual[4]['metadata']['iStartLineNumber'])
        self.assertEqual(34, lActual[4]['metadata']['iEndLineNumber'])
        self.assertEqual(1, len(lActual[5]['lines']))
        self.assertEqual(lActual[5]['lines'][0].line, 'context c1 is library ieee; use ieee.std_logic_1164; end;')
        self.assertEqual(lActual[6]['lines'][0].line, 'context c1 is library ieee; use ieee.std_logic_1164; end context;')
        self.assertEqual(lActual[7]['lines'][0].line, 'context c1 is library ieee; use ieee.std_logic_1164; end context c1;')
        self.assertEqual(37, lActual[5]['metadata']['iStartLineNumber'])
        self.assertEqual(37, lActual[5]['metadata']['iEndLineNumber'])
