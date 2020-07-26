import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','library','library_classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_library(unittest.TestCase):

    def test_library_keyword(self):
        lExpected = []
        lExpected.append((3,0))
        lExpected.append((5,0))
        lExpected.append((7,0))
        lExpected.append((7,5))
        lExpected.append((7,10))

        lExpected.append((9,0))

        lExpected.append((12,0))
        lExpected.append((12,10))
        lExpected.append((12,20))

        lExpected.append((14,0))

        lExpected.append((21,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.library_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_library_logical_name(self):
        lExpected = []
        lExpected.append((3,2))

        lExpected.append((5,2))
        lExpected.append((5,5))
        lExpected.append((5,8))

        lExpected.append((7,2))
        lExpected.append((7,7))
        lExpected.append((7,12))

        lExpected.append((9,2))

        lExpected.append((12,2))
        lExpected.append((12,12))
        lExpected.append((12,22))

        lExpected.append((15,0))

        lExpected.append((22,0))
        lExpected.append((24,0))
        lExpected.append((26,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.library_logical_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_library_semicolon(self):
        lExpected = []
        lExpected.append((3,3))

        lExpected.append((5,9))

        lExpected.append((7,3))
        lExpected.append((7,8))
        lExpected.append((7,13))

        lExpected.append((9,3))

        lExpected.append((12,3))
        lExpected.append((12,13))
        lExpected.append((12,23))

        lExpected.append((16,0))

        lExpected.append((27,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.library_semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_library_comma(self):
        lExpected = []
        lExpected.append((5,3))
        lExpected.append((5,6))

        lExpected.append((23,0))
        lExpected.append((25,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.library_comma):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

