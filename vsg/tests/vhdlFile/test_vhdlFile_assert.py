import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','assert_statement','assert_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileMethods(unittest.TestCase):

    def test_isAssertKeyword_assignment(self):
        lExpected = [6,10,15,19,26]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isAssertKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isAssertEnd_assignment(self):
        lExpected = [8,12,17,21,27]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isAssertEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideAssert_assignment(self):
        lExpected = [6,7,8,10,11,12,15,16,17,19,20,21,26,27]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideAssert:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_indent(self):
        lExpected = [None,1,1,None,2,3,None,1,None]
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex > 21 and iIndex < 31:
                lActual.append(oLine.indentLevel)
        self.assertEqual(lActual, lExpected)

    def test_sequential(self):
        lExpected = []
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideSequential:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
