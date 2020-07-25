import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','context_reference','context_reference_classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_context(unittest.TestCase):

    def test_context_reference_keyword(self):
        lExpected = []
        lExpected.append((4,1))
        lExpected.append((11,1))
        lExpected.append((26,1))
        lExpected.append((40,16))
        lExpected.append((55,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_reference_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_reference_identifier(self):
        lExpected = []
        lExpected.append((4,3))
        lExpected.append((11,3))
        lExpected.append((11,5))
        lExpected.append((26,3))
        lExpected.append((26,5))
        lExpected.append((40,18))
        lExpected.append((40,20))
        lExpected.append((56,0))
        lExpected.append((58,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_reference_identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_reference_comma(self):
        lExpected = []
        lExpected.append((11,4))
        lExpected.append((26,4))
        lExpected.append((40,19))
        lExpected.append((57,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_reference_comma):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_context_reference_semicolon(self):
        lExpected = []
        lExpected.append((4,4))
        lExpected.append((11,6))
        lExpected.append((26,6))
        lExpected.append((40,21))
        lExpected.append((59,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.context_reference_semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)
