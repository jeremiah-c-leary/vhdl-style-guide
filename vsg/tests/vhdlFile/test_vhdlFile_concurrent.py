import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFileConcurrent = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFileConcurrent = vhdlFile.vhdlFile(lFileConcurrent)

class testVhdlFileMethods(unittest.TestCase):

    def test_insideConcurrent_assignment(self):
        lExpected = [6,7,8,9,10,11,23,24,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42,44,45,46,48,50,51,52,53,54,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.insideConcurrent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConcurrentBegin_assignment(self):
        lExpected = [6,7,8,9,11,23,24,26,32,33,34,35,38,39,42,44,45,48,50]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.isConcurrentBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndConcurrent_assignment(self):
        lExpected = [6,7,8,10,11,23,24,30,32,33,34,36,38,41,42,44,46,48,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.isEndConcurrent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_hasConcurrentLabel_assignment(self):
        lExpected = [32,33,34,35]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.hasConcurrentLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
