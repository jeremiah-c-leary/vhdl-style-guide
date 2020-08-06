import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import package_body


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','package_body','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_package_body_parsing(unittest.TestCase):

    def test_package_body_package_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((6,0))
        lExpected.append((10,0))
        lExpected.append((14,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.package_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_body_keyword(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((6,2))
        lExpected.append((10,2))
        lExpected.append((15,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.body_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_simple_name(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((6,4))
        lExpected.append((10,4))
        lExpected.append((16,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.simple_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_is_keyword(self):
        lExpected = []
        lExpected.append((2,6))
        lExpected.append((6,6))
        lExpected.append((10,6))
        lExpected.append((17,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.is_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_end_keyword(self):
        lExpected = []
        lExpected.append((4,0))
        lExpected.append((8,0))
        lExpected.append((12,0))
        lExpected.append((18,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.end_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_end_package_keyword(self):
        lExpected = []
        lExpected.append((4,2))
        lExpected.append((12,2))
        lExpected.append((19,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.end_package_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_end_body_keyword(self):
        lExpected = []
        lExpected.append((4,4))
        lExpected.append((12,4))
        lExpected.append((20,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.end_body_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_end_simple_name(self):
        lExpected = []
        lExpected.append((4,6))
        lExpected.append((21,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.end_simple_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_package_body_semicolon(self):
        lExpected = []
        lExpected.append((4,7))
        lExpected.append((8,1))
        lExpected.append((12,5))
        lExpected.append((22,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, package_body.semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

