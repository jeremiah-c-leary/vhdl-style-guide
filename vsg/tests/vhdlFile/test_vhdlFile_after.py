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


        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideClockProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
