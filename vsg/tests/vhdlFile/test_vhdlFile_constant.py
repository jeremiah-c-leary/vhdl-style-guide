import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

lFileConstant = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))
oFileConstant = vhdlFile.vhdlFile(lFileConstant)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','constant','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileConstantMethods(unittest.TestCase):

    def test_isConstant_assignment(self):
        lExpected = [5,6,7,8,9,10,17,18,28,30,38,40,43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstantEnd_assignment(self):
        lExpected = [5,6,7,8,9,11,17,18,28,36,38,41,44]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstantEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideConstant_assignment(self):
        lExpected = [5,6,7,8,9,10,11,17,18,28,30,31,32,33,34,35,36,38]
        lExpected.extend(range(40, 42))
        lExpected.extend(range(43, 45))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.insideConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstantArray_assignment(self):
        lExpected = []
        lExpected.extend(range(30,37))
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstantArray:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_constant_keyword(self):
        lExpected = []
        lExpected.append((2,0))
        lExpected.append((4,0))
        lExpected.append((6,0))
        lExpected.append((8,0))
        lExpected.append((10,0))
        lExpected.append((22,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_identifier(self):
        lExpected = []
        lExpected.append((2,2))
        lExpected.append((4,2))
        lExpected.append((6,2))
        lExpected.append((8,2))
        lExpected.append((8,5))
        lExpected.append((8,8))
        lExpected.append((11,0))
        lExpected.append((13,0))
        lExpected.append((15,0))
        lExpected.append((23,0))
        lExpected.append((25,0))
        lExpected.append((27,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_comma(self):
        lExpected = []
        lExpected.append((8,3))
        lExpected.append((8,6))
        lExpected.append((12,0))
        lExpected.append((14,0))
        lExpected.append((24,0))
        lExpected.append((26,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_comma):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_colon(self):
        lExpected = []
        lExpected.append((2,4))
        lExpected.append((4,4))
        lExpected.append((6,4))
        lExpected.append((8,10))
        lExpected.append((16,0))
        lExpected.append((28,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_colon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_subtype_indication(self):
        lExpected = []
        lExpected.append((2,6))

        lExpected.append((4,6))
        lExpected.append((4,7))
        lExpected.append((4,8))
        lExpected.append((4,10))
        lExpected.append((4,12))
        lExpected.append((4,13))

        lExpected.append((6,6))
        lExpected.append((6,7))
        lExpected.append((6,8))
        lExpected.append((6,10))
        lExpected.append((6,12))
        lExpected.append((6,13))

        lExpected.append((8,12))

        lExpected.append((17,0))

        lExpected.append((29,0))
        lExpected.append((29,1))
        lExpected.append((29,3))
        lExpected.append((29,5))
        lExpected.append((29,7))
        lExpected.append((29,9))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_subtype_indication):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_assignment_operator(self):
        lExpected = []
        lExpected.append((6,15))
        lExpected.append((8,14))
        lExpected.append((18,0))
        lExpected.append((30,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_assignment_operator):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_assignment_expression(self):
        lExpected = []
        lExpected.append((6,17))
        lExpected.append((8,16))
        lExpected.append((19,0))
        lExpected.append((31,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_assignment_expression):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_constant_semicolon(self):
        lExpected = []
        lExpected.append((2,7))
        lExpected.append((4,14))
        lExpected.append((6,18))
        lExpected.append((8,17))
        lExpected.append((20,0))
        lExpected.append((32,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, parser.constant_semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)
