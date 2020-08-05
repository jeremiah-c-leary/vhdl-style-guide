import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import architecture_body


lFileArchitecture = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_test_input.vhd'))
oFileArchitecture = vhdlFile.vhdlFile(lFileArchitecture)

lFileArch2 = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','rule_029_test_input.vhd'))
oFileArch2 = vhdlFile.vhdlFile(lFileArch2)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileMethods(unittest.TestCase):

    def test_insideArchitecture_assignment(self):
        lExpected = [3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,81,82,83,84,85]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.insideArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureBegin_assignment(self):
        lExpected = [5,11,16,22,29,34,39,49,61,83]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureKeyword_assignment(self):
        lExpected = [3,9,14,20,26,33,37,47,59,81]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment(self):
        lExpected = [7,13,18,24,31,35,45,55,77,85]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitectureDeclarativeRegion(self):
        lExpected = []
        lExpected.extend(range(3,6))
        lExpected.extend(range(9,12))
        lExpected.extend(range(14,17))
        lExpected.extend(range(20,23))
        lExpected.extend(range(26,30))
        lExpected.extend(range(33,35))
        lExpected.extend(range(37,40))
        lExpected.extend(range(47,50))
        lExpected.extend(range(59,62))
        lExpected.extend(range(81,84))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.insideArchitectureDeclarativeRegion:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitectureDeclarativeRegion_2(self):
        lExpected = []
        lExpected.extend(range(2,59))
        lExpected.extend(range(64,120))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArch2.lines):
            if oLine.insideArchitectureDeclarativeRegion:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_architecture_keyword(self):
        lExpected = []
        lExpected.append((3,0))
        lExpected.append((11,0))
        lExpected.append((18,0))
        lExpected.append((25,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_semicolon(self):
        lExpected = []
        lExpected.append((7,5))
        lExpected.append((15,1))
        lExpected.append((22,3))
        lExpected.append((34,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.semicolon):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_end_keyword(self):
        lExpected = []
        lExpected.append((7,0))
        lExpected.append((15,0))
        lExpected.append((22,0))
        lExpected.append((31,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.end_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_end_architecture_keyword(self):
        lExpected = []
        lExpected.append((7,2))
        lExpected.append((22,2))
        lExpected.append((32,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.end_architecture_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_simple_name(self):
        lExpected = []
        lExpected.append((7,4))
        lExpected.append((33,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.simple_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_identifier(self):
        lExpected = []
        lExpected.append((3,2))
        lExpected.append((11,2))
        lExpected.append((18,2))
        lExpected.append((26,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.identifier):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_of_keyword(self):
        lExpected = []
        lExpected.append((3,4))
        lExpected.append((11,4))
        lExpected.append((18,4))
        lExpected.append((27,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.of_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_entity_name(self):
        lExpected = []
        lExpected.append((3,6))
        lExpected.append((11,6))
        lExpected.append((18,6))
        lExpected.append((28,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.entity_name):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_is_keyword(self):
        lExpected = []
        lExpected.append((3,8))
        lExpected.append((11,8))
        lExpected.append((18,8))
        lExpected.append((29,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.is_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

    def test_architecture_begin_keyword(self):
        lExpected = []
        lExpected.append((5,0))
        lExpected.append((13,0))
        lExpected.append((20,0))
        lExpected.append((30,0))

        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            for iItem, oItem in enumerate(lLine.objects):
                if isinstance(oItem, architecture_body.begin_keyword):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)
