import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import component


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','component','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_component_parsing(unittest.TestCase):

    def test_component_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((8,0))
        lExpected.append((12,0))
        lExpected.append((16,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_component_identifier(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((8,2))
        lExpected.append((12,2))
        lExpected.append((16,2))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_component_is_keyword(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((8,4))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.is_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_component_end_keyword(self):
        lExpected = []
        lExpected.append((4,0))
        lExpected.append((10,0))
        lExpected.append((14,0))
        lExpected.append((18,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.end_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_component_end_component_keyword(self):
        lExpected = []
        lExpected.append((4,2))
        lExpected.append((10,2))
        lExpected.append((14,2))
        lExpected.append((18,2))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.end_component_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_component_simple_name(self):
        lExpected = []
        lExpected.append((4,4))
        lExpected.append((14,4))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.simple_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_component_semicolon(self):
        lExpected = []
        lExpected.append((4,5))
        lExpected.append((10,3))
        lExpected.append((14,5))
        lExpected.append((18,3))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, component.semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

