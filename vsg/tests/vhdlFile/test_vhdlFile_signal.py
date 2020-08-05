import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser
from vsg.token import signal_declaration


lFileSignal = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))
oFileSignal = vhdlFile.vhdlFile(lFileSignal)

lFileMultiSignal = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','signal','multi_line_signal_test_input.vhd'))
oFileMultiSignal = vhdlFile.vhdlFile(lFileMultiSignal)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','signal','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testVhdlFileMethods(unittest.TestCase):

    def test_isSignal_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,23]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileSignal.lines):
            if oLine.isSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

        lExpected = [5,8,18,20,23,27,32,40,42,45,49,54,60,67,75,78,79]
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiSignal.lines):
            if oLine.isSignal:
                lActual.append(iIndex)
        self.assertEqual(lActual, lExpected)

    def test_insideSignal_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,23]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileSignal.lines):
            if oLine.insideSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

        lExpected = [5,6,8,9,10,11,12,13,18,20,21]
        lExpected.extend(range(23,26))
        lExpected.extend(range(27,31))
        lExpected.extend(range(32,37))
        lExpected.append(40)
        lExpected.extend(range(42,44))
        lExpected.extend(range(45,48))
        lExpected.extend(range(49,53))
        lExpected.extend(range(54,59))
        lExpected.extend(range(60,66))
        lExpected.extend(range(67,74))
        lExpected.append(75)
        lExpected.extend([78,79])
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiSignal.lines):
            if oLine.insideSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndSignal_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,23]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileSignal.lines):
            if oLine.isEndSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

        lExpected = [6,13,18,21,25,30,36,40,43,47,52,58,65,73,75,78,79]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiSignal.lines):
            if oLine.isEndSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_signal_keyword(self):
        lExpected = []
        lExpected.append((5,0))
        lExpected.append((7,0))
        lExpected.append((9,0))
        lExpected.append((11,0))
        lExpected.append((13,0))
        lExpected.append((25,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_identifier(self):
        lExpected = []
        lExpected.append((5,2))
        lExpected.append((7,2))
        lExpected.append((9,2))
        lExpected.append((11,2))
        lExpected.append((11,5))
        lExpected.append((11,8))
        lExpected.append((14,0))
        lExpected.append((16,0))
        lExpected.append((18,0))
        lExpected.append((26,0))
        lExpected.append((28,0))
        lExpected.append((30,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_comma(self):
        lExpected = []
        lExpected.append((11,3))
        lExpected.append((11,6))
        lExpected.append((15,0))
        lExpected.append((17,0))
        lExpected.append((27,0))
        lExpected.append((29,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.comma):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_colon(self):
        lExpected = []
        lExpected.append((5,4))
        lExpected.append((7,4))
        lExpected.append((9,4))
        lExpected.append((11,10))
        lExpected.append((19,0))
        lExpected.append((31,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.colon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_subtype_indication(self):
        lExpected = []
        lExpected.append((5,6))

        lExpected.append((7,6))
        lExpected.append((7,7))
        lExpected.append((7,8))
        lExpected.append((7,10))
        lExpected.append((7,12))
        lExpected.append((7,13))

        lExpected.append((9,6))
        lExpected.append((9,7))
        lExpected.append((9,8))
        lExpected.append((9,10))
        lExpected.append((9,12))
        lExpected.append((9,13))

        lExpected.append((11,12))

        lExpected.append((20,0))

        lExpected.append((32,0))
        lExpected.append((32,1))
        lExpected.append((32,3))
        lExpected.append((32,5))
        lExpected.append((32,7))
        lExpected.append((32,9))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.subtype_indication):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_assignment_operator(self):
        lExpected = []
        lExpected.append((9,15))
        lExpected.append((11,14))
        lExpected.append((21,0))
        lExpected.append((33,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.assignment_operator):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_assignment_expression(self):
        lExpected = []
        lExpected.append((9,17))
        lExpected.append((11,16))
        lExpected.append((22,0))
        lExpected.append((34,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.assignment_expression):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_signal_semicolon(self):
        lExpected = []
        lExpected.append((5,7))
        lExpected.append((7,14))
        lExpected.append((9,18))
        lExpected.append((11,17))
        lExpected.append((23,0))
        lExpected.append((35,0))

#        utils.print_objects(oFile, True)

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, signal_declaration.semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)
