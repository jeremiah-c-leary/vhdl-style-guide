import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))

class testVhdlFileTypeAssignments(unittest.TestCase):


    def test_isTypeKeyword(self):
        lExpected = [4,6,11,13,27,29,34,36,43,54,57,69]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeEnd(self):
        lExpected = [4,9,11,19,27,32,34,40,48,55,62,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeEnumeratedKeyword(self):
        lExpected = [4,6,27,29,36,43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeEnumeratedKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeEnumeratedEnd(self):
        lExpected = [4,9,27,32,40,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeEnumeratedEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideTypeEnumerated(self):
        lExpected = [4,6,7,8,9,27,29,30,31,32,36,37,38,39,40,43,44,45,46,47,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideTypeEnumerated:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_TypeIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,  10,11,  12,13,14,15,16,17,  18,19,   20]
        lExpected = [None,None,0,None,1,None,1,2,2,2,None, 1,None, 1, 2, 2, 2, 2,None, 1, None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSubtypeKeyword(self):
        lExpected = [51,65]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSubtypeKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSubtypeEnd(self):
        lExpected = [51,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSubtypeEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideSubtype(self):
        lExpected = [51,65,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideSubtype:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeArrayKeyword(self):
        lExpected = [54]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeArrayKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeArrayEnd(self):
        lExpected = [55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeArrayEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideTypeArray(self):
        lExpected = [54,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideTypeArray:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_isTypeRecordKeyword(self):
        lExpected = [13,57,70]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeRecordKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeRecordEnd(self):
        lExpected = [19,62,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeRecordEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideTypeRecord(self):
        lExpected = [13,14,15,16,17,18,19,57,58,59,60,61,62,70,71,72,73,74,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideTypeRecord:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture(self):
        lExpected = [23]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
