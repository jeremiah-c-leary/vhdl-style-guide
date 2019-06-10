import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','after','after_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileAfterMethods(unittest.TestCase):

    def test_after_detection(self):
        lExpected = []
        lExpected.extend(range(15, 19))
        lExpected.extend([32,35])
        lExpected.extend(range(49, 53))
        lExpected.extend(range(66, 70))
        lExpected.append(74)
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasAfterKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_inside_clock_process(self):
        lExpected = []
        lExpected.extend(range(14, 21))
        lExpected.extend(range(31, 38))
        lExpected.extend(range(48, 55))
        lExpected.extend(range(65, 72))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideClockProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
