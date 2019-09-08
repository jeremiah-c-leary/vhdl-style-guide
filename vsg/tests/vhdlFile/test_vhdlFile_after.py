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
        lExpected.append(50)
        lExpected.append(52)
        lExpected.append(56)
        lExpected.append(61)
        lExpected.extend(range(76, 80))
        lExpected.extend(range(93, 97))
        lExpected.append(101)
        lExpected.extend(range(109, 113))
        lExpected.extend(range(121, 125))
        lExpected.extend(range(133, 137))
        lExpected.append(145)
        lExpected.append(147)
        lExpected.extend(range(150, 154))
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
        lExpected.extend(range(48, 64))
        lExpected.extend(range(75, 82))
        lExpected.extend(range(92, 99))
        lExpected.extend(range(108, 115))
        lExpected.extend(range(120, 127))
        lExpected.extend(range(132, 139))
        lExpected.extend(range(149, 156))


        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideClockProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_inside_reset_process(self):
        lExpected = []
        lExpected.extend(range(9, 14))
        lExpected.extend(range(26, 31))
        lExpected.extend(range(43, 48))
        lExpected.extend(range(70, 75))
        lExpected.extend(range(87, 92))
        lExpected.extend(range(144, 149))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideResetProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
