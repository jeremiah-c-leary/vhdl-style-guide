import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','when','when_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile) 


class testVhdlFileWhenAssignments(unittest.TestCase):


    def test_insideWhen_assignment(self):
        lExpected = range(13,17)
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideWhen:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isWhenKeyword_assignment(self):
        lExpected = range(13,16)
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWhenKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isWhenElseKeyword_assignment(self):
        lExpected = range(14,17)
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWhenElseKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isWhenEnd_assignment(self):
        lExpected = [16]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWhenEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
