import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
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

