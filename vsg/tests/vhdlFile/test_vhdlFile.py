import os

import unittest
from vsg import vhdlFile

sFileLibraryName = os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd')
oFileLibrary = vhdlFile.vhdlFile(sFileLibraryName)

oFileSignal = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))

oFileProcess = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))
oFilePort = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','generic','generic_test_input.vhd'))
oFileEntity = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','entity','entity_test_input.vhd'))
oFileConcurrent = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFileArchitecture = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_test_input.vhd'))
oFileArchitectureLoop = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_loop_test_input.vhd'))
oFileArchitectureFunctionLoop = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_loop_in_function_test_input.vhd'))
oFileFunction = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','function','function_test_input.vhd'))
oFileWhitespace = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','whitespace','whitespace_test_input.txt'))

class testVhdlFileMethods(unittest.TestCase):

    def test_vhdlFile_class_exists(self):
        self.assertTrue(oFileLibrary)
        self.assertEqual(oFileLibrary.filename, sFileLibraryName)

    def test_loading_of_file(self):

        # Read in test file used for all tests
        lExpected = ['']
        with open(sFileLibraryName) as oExpectedFile:
            for sLine in oExpectedFile:
                lExpected.append(sLine.rstrip())
        oExpectedFile.close()
        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            self.assertEqual(oLine.line, lExpected[iIndex])

    def test_blank_line_assignment(self):

        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex == 1 or iIndex == 2 or iIndex == 6 or iIndex == 8 or iIndex == 11 or \
               iIndex == 12 or iIndex == 15 or iIndex == 17 or iIndex == 18 or iIndex == 19 or \
               iIndex == 22 or iIndex == 25 or iIndex == 28 or iIndex == 29 or iIndex == 31:
                self.assertTrue(oLine.isBlank)
            else:
                self.assertFalse(oLine.isBlank)

    def test_library_assignment(self):
        lExpected = [3,7,9,13,20,21]
        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibrary)
                self.assertEqual(oLine.indentLevel, 0)
            else:
                self.assertFalse(oLine.isLibrary)

    def test_library_use_assignment(self):
        lExpected = [4,5,10,14,16,23,24,26,27,30]
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


    def test_insideEntity_assignment(self):
        lExpected = [0,1,2,17,18,48,64,79,92,93,104,105,106,107,108,109,110,111,112,124,125,126,134,135,136,137,147]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileEntity.lines):
            if not oLine.insideEntity:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEntityDeclaration_assignment(self):
        lExpected = [3,19,34,49,65,80,94,113,127,138]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileEntity.lines):
            if oLine.isEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndEntityDeclaration_assignment(self):
        lExpected = [16,33,47,63,78,91,103,123,133,146]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileEntity.lines):
            if oLine.isEndEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

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
        lExpected = [8,9,10,11,12,13,14,15,25,26,27,28,29,30,31,39,40,41,42,43,44,45,46,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,86,87,88,89,90,98,99,100,101,102,118,119,120,121,122,128,129,130,131,132,133,140,141,142,143,144,150,151,152,153,159,160,161,162]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.insidePortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortKeyword_assignment(self):
        lExpected = [8,25,39,56,70,86,98,118,128,140,150,159]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPortMap_assignment(self):
        lExpected = [15,31,46,62,77,90,102,122,133,144,153,162]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isEndPortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        lExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131,141,142,152,161]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isPortDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_insideGenericMap_assignment(self):
        lExpected = [4,5,6,7,20,21,22,23,35,36,37,38,51,52,53,54,66,67,68,69,82,83,84,85,95,96,97,114,115,116,117,139,140,141,153,154,155,156,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.insideGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericKeyword_assignment(self):
        lExpected = [4,20,35,51,66,82,95,114,139,153]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isGenericKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndGenericMap_assignment(self):
        lExpected = [7,23,38,54,69,85,97,117,141,157]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isEndGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericDeclaration_assignment(self):
        lExpected = [5,6,21,22,36,37,52,53,67,68,83,84,96,97,116,139,140,155,156]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isGenericDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitecture_assignment(self):
        lExpected = [3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,59,60,61,62,63,64,65,66,67,68,69,70,71]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.insideArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureBegin_assignment(self):
        lExpected = [5,11,16,22,29,34,39,49,61]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureKeyword_assignment(self):
        lExpected = [3,9,14,20,26,33,37,47,59]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment(self):
        lExpected = [7,13,18,24,31,35,45,55,71]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment_with_loop(self):
        lExpected = [11]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitectureLoop.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment_with_loop_inside_function(self):
        lExpected = [21]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitectureFunctionLoop.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_function_assignment(self):
        lExpected = [122]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileFunction.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSignal_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,23]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileSignal.lines):
            if oLine.isSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideConcurrent_assignment(self):
        lExpected = [6,7,8,9,10,11,23,24,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42,44,45,46,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.insideConcurrent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConcurrentBegin_assignment(self):
        lExpected = [6,7,8,9,11,23,24,26,32,33,34,35,38,39,42,44,45,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.isConcurrentBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndConcurrent_assignment(self):
        lExpected = [6,7,8,10,11,23,24,30,32,33,34,36,38,41,42,44,46,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.isEndConcurrent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_hasEntity_assignment(self):
        self.assertFalse(oFileConcurrent.hasEntity)
        self.assertTrue(oFilePort.hasEntity)
        self.assertTrue(oFileEntity.hasEntity)

    def test_hasArchitecture_assignment(self):
        self.assertFalse(oFileWhitespace.hasArchitecture)
        self.assertTrue(oFileConcurrent.hasArchitecture)
        self.assertTrue(oFileProcess.hasArchitecture)
