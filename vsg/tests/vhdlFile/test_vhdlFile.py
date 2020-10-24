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


    def test_hasArchitecture_assignment(self):
        self.assertFalse(oFileWhitespace.hasArchitecture)
        self.assertTrue(oFileConcurrent.hasArchitecture)
        self.assertTrue(oFileProcess.hasArchitecture)
