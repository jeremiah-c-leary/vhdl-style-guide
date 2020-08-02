import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import entity as token


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','entity','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_entity_parsing(unittest.TestCase):

    def test_entity_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((9,0))
        lExpected.append((15,0))
        lExpected.append((21,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_entity_semicolon(self):
        lExpected = []
        lExpected.append((6,5))
        lExpected.append((13,1))
        lExpected.append((19,3))
        lExpected.append((28,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_entity_end_keyword(self):
        lExpected = []
        lExpected.append((6,0))
        lExpected.append((13,0))
        lExpected.append((19,0))
        lExpected.append((25,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.end_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_entity_end_entity_keyword(self):
        lExpected = []
        lExpected.append((6,2))
        lExpected.append((19,2))
        lExpected.append((26,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.end_entity_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_entity_simple_name(self):
        lExpected = []
        lExpected.append((6,4))
        lExpected.append((27,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.simple_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_entity_identifier(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((9,2))
        lExpected.append((15,2))
        lExpected.append((22,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_entity_begin_keyword(self):
        lExpected = []
        lExpected.append((4,0))
        lExpected.append((11,0))
        lExpected.append((17,0))
        lExpected.append((24,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, token.begin_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)
