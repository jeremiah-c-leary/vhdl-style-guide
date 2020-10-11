import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

sFileLibraryName = os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd')
lFileLibrary = utils.read_vhdlfile(sFileLibraryName)
oFileLibrary = vhdlFile.vhdlFile(lFileLibrary)

lFileProcess = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(lFileProcess)
lFilePort = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))
oFilePort = vhdlFile.vhdlFile(lFilePort)
lFileGeneric = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generic','generic_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(lFileGeneric)
lFileConcurrent = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFileConcurrent = vhdlFile.vhdlFile(lFileConcurrent)
lFileArchitectureFunctionLoop = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_loop_in_function_test_input.vhd'))
oFileArchitectureFunctionLoop = vhdlFile.vhdlFile(lFileArchitectureFunctionLoop)
lFileWhitespace = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','whitespace','whitespace_test_input.txt'))
oFileWhitespace = vhdlFile.vhdlFile(lFileWhitespace)

class testVhdlFileMethods(unittest.TestCase):

    def test_vhdlFile_class_exists(self):
        self.assertTrue(oFileLibrary)


    def test_blank_line_assignment(self):

        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex == 1 or iIndex == 2 or iIndex == 6 or iIndex == 8 or iIndex == 11 or \
               iIndex == 12 or iIndex == 15 or iIndex == 17 or iIndex == 18 or iIndex == 19 or \
               iIndex == 22 or iIndex == 25 or iIndex == 28 or iIndex == 29 or iIndex == 31 or iIndex == 35:
                self.assertTrue(oLine.isBlank)
            else:
                self.assertFalse(oLine.isBlank)

    def test_library_use_assignment(self):
        lExpected = [4,5,10,14,16,23,24,26,27,30,34,38]
        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibraryUse)
                self.assertEqual(oLine.indentLevel, 1)
            else:
                self.assertFalse(oLine.isLibraryUse)

    def test_library_use_assignment_in_port_map(self):
        '''
        This tests for an error condition in which port names that started with "use" were
        classified as a library use statement.
        '''
        lExpected = []
        # Compare
        for iIndex, oLine in enumerate(oFilePort.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibraryUse)     # pragma: no cover
                self.assertEqual(oLine.indentLevel, 1)  # pragma: no cover
            else:
                self.assertFalse(oLine.isLibraryUse)


    def test_port_map_indent(self):
        #           [   0,   1,   2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,  17]
        lExpected = [None,None,None,0,1,2,2,1,1,2, 2, 2, 2, 2, 2, 1, 0,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFilePort.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insidePortMap_assignment(self):
        lExpected = [8,9,10,11,12,13,14,15,25,26,27,28,29,30,31,39,40,41,42,43,44,45,46,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,86,87,88,89,90,98,99,100,101,102,118,119,120,121,122,128,129,130,131,132,133,140,141,142,143,144,150,151,152,153,159,160,161,162,168,169,170,171,172,173,174]
        lExpected.extend(range(180, 189))
        lExpected.extend(range(198, 203))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.insidePortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortKeyword_assignment(self):
        lExpected = [8,25,39,56,70,86,98,118,128,140,150,159,168,180,198]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPortMap_assignment(self):
        lExpected = [15,31,46,62,77,90,102,122,133,144,153,162,174,188,202]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isEndPortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        lExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131,141,142,152,161,169,170,171,172,173]
        lExpected.extend(range(181, 186))
        lExpected.extend(range(199, 202))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isPortDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_insideGenericMap_assignment(self):
        lExpected = [4,5,6,7,20,21,22,23,35,36,37,38,51,52,53,54,66,67,68,69,82,83,84,85,95,96,97,114,115,116,117,139,140,141,153,154,155,156,157]
        lExpected.extend(range(168, 175))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.insideGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericKeyword_assignment(self):
        lExpected = [4,20,35,51,66,82,95,114,139,153,168]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isGenericKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndGenericMap_assignment(self):
        lExpected = [7,23,38,54,69,85,97,117,141,157,174]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isEndGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericDeclaration_assignment(self):
        lExpected = [5,6,21,22,36,37,52,53,67,68,83,84,96,97,116,139,140,155,156]
        lExpected.extend(range(170,172))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isGenericDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_hasArchitecture_assignment(self):
        self.assertFalse(oFileWhitespace.hasArchitecture)
        self.assertTrue(oFileConcurrent.hasArchitecture)
        self.assertTrue(oFileProcess.hasArchitecture)
