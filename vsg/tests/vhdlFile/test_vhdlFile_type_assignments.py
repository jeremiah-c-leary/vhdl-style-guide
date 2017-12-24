import os

import unittest
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))

class testVhdlFileTypeAssignments(unittest.TestCase):


    def test_isTypeKeyword(self):
        lExpected = [4,6,11,19,21,26,28,35,46,49]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeEnd(self):
        lExpected = [4,9,11,19,24,26,32,40,47,54]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideType(self):
        lExpected = [4,6,7,8,9,11,19,21,22,23,24,26,28,29,30,31,32,35,36,37,38,39,40]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideType:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_TypeIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,  10,11,  12]
        lExpected = [None,None,0,None,1,None,1,2,2,2,None, 1,None]
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
        lExpected = [43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSubtypeKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSubtypeEnd(self):
        lExpected = [43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSubtypeEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideSubtype(self):
        lExpected = [43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideSubtype:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeArrayKeyword(self):
        lExpected = [46]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeArrayKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeArrayEnd(self):
        lExpected = [47]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeArrayEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideTypeArray(self):
        lExpected = [46,47]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideTypeArray:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_isTypeRecordKeyword(self):
        lExpected = [49]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeRecordKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isTypeRecordEnd(self):
        lExpected = [54]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isTypeRecordEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideTypeRecord(self):
        lExpected = [49,50,51,52,53,54]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideTypeRecord:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
