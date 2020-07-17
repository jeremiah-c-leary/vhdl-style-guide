import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFileArchitecture = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_test_input.vhd'))
oFileArchitecture = vhdlFile.vhdlFile(lFileArchitecture)

lFileArch2 = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','rule_029_test_input.vhd'))
oFileArch2 = vhdlFile.vhdlFile(lFileArch2)

class testVhdlFileMethods(unittest.TestCase):

    def test_insideArchitecture_assignment(self):
        lExpected = [3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,81,82,83,84,85]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.insideArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureBegin_assignment(self):
        lExpected = [5,11,16,22,29,34,39,49,61,83]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureKeyword_assignment(self):
        lExpected = [3,9,14,20,26,33,37,47,59,81]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment(self):
        lExpected = [7,13,18,24,31,35,45,55,77,85]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitectureDeclarativeRegion(self):
        lExpected = []
        lExpected.extend(range(3,6))
        lExpected.extend(range(9,12))
        lExpected.extend(range(14,17))
        lExpected.extend(range(20,23))
        lExpected.extend(range(26,30))
        lExpected.extend(range(33,35))
        lExpected.extend(range(37,40))
        lExpected.extend(range(47,50))
        lExpected.extend(range(59,62))
        lExpected.extend(range(81,84))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.insideArchitectureDeclarativeRegion:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitectureDeclarativeRegion_2(self):
        lExpected = []
        lExpected.extend(range(2,59))
        lExpected.extend(range(64,120))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArch2.lines):
            if oLine.insideArchitectureDeclarativeRegion:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
