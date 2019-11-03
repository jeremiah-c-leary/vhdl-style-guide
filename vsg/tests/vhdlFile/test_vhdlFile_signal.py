import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFileSignal = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))
oFileSignal = vhdlFile.vhdlFile(lFileSignal)

lFileMultiSignal = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','signal','multi_line_signal_test_input.vhd'))
oFileMultiSignal = vhdlFile.vhdlFile(lFileMultiSignal)

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

        lExpected = [5,8]
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

        lExpected = [5,6,8,9,10,11,12,13]
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

        lExpected = [6,13]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileMultiSignal.lines):
            if oLine.isEndSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

