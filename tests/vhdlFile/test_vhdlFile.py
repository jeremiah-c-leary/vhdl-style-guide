
import unittest
from modules import vhdlFile

class testVhdlFileMethods(unittest.TestCase):

    def test_vhdlFile_class_exists(self):
        oFile = vhdlFile.vhdlFile('tests/rule_library/library_test_input.vhd')
        self.assertTrue(oFile)
        self.assertEqual(oFile.filename, 'tests/rule_library/library_test_input.vhd')

    def test_loading_of_file(self):
        oFile = vhdlFile.vhdlFile('tests/rule_library/library_test_input.vhd')

        # Read in test file used for all tests
        lExpected = ['']
        with open('tests/rule_library/library_test_input.vhd') as oExpectedFile:
            for sLine in oExpectedFile:
                lExpected.append(sLine.rstrip())
        oExpectedFile.close()
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            self.assertEqual(oLine.line, lExpected[iIndex])

    def test_blank_line_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_library/library_test_input.vhd')

        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == 1 or iIndex == 2 or iIndex == 6 or iIndex == 8 or iIndex == 11 or \
               iIndex == 12 or iIndex == 15 or iIndex == 17 or iIndex == 18 or iIndex == 19 or \
               iIndex == 22 or iIndex == 25 or iIndex == 28 or iIndex == 30:
                self.assertTrue(oLine.isBlank)
            else:
                self.assertFalse(oLine.isBlank)

    def test_library_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_library/library_test_input.vhd')
        lExpected = [3,7,9,13,20,21]
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibrary)
                self.assertEqual(oLine.indentLevel, 0)
            else:
                self.assertFalse(oLine.isLibrary)

    def test_library_use_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_library/library_test_input.vhd')
        lExpected = [4,5,10,14,16,23,24,26,27,29]
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibraryUse)
                self.assertEqual(oLine.indentLevel, 1)
            else:
                self.assertFalse(oLine.isLibraryUse)

    def test_insideEntity_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_entity/entity_test_input.vhd')
        lExpected = [0,1,2,17,18,48,64,79,92,93,104,105,106,107,108,109,110,111,112,124,125,126,134,135]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if not oLine.insideEntity:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEntityDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_entity/entity_test_input.vhd')
        lExpected = [3,19,34,49,65,80,94,113,127]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndEntityDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_entity/entity_test_input.vhd')
        lExpected = [16,33,47,63,78,91,103,123,133]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insidePortMap_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_port/port_test_input.vhd')
        lExpected = [8,9,10,11,12,13,14,15,25,26,27,28,29,30,31,39,40,41,42,43,44,45,46,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,86,87,88,89,90,98,99,100,101,102,118,119,120,121,122,128,129,130,131,132]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insidePortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_port/port_test_input.vhd')
        lExpected = [8,25,39,56,70,86,98,118,128]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPortMap_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_port/port_test_input.vhd')
        lExpected = [15,31,46,62,77,90,102,122,132]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_port/port_test_input.vhd')
        lExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_insideGenericMap_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_generic/generic_test_input.vhd')
        lExpected = [4,5,6,7,20,21,22,23,35,36,37,38,51,52,53,54,66,67,68,69,82,83,84,85,95,96,97,114,115,116,117]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_generic/generic_test_input.vhd')
        lExpected = [4,20,35,51,66,82,95,114]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndGenericMap_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_generic/generic_test_input.vhd')
        lExpected = [7,23,38,54,69,85,97,117]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_generic/generic_test_input.vhd')
        lExpected = [5,6,21,22,36,37,52,53,67,68,83,84,96,97,115,116]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitecture_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_architecture/architecture_test_input.vhd')
        lExpected = [3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,28,29,30,31,33,34,35]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureBegin_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_architecture/architecture_test_input.vhd')
        lExpected = [5,11,16,22,29,34]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_architecture/architecture_test_input.vhd')
        lExpected = [3,9,14,20,26,33]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_architecture/architecture_test_input.vhd')
        lExpected = [7,13,18,24,31,35]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSignal_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_signal/signal_test_input.vhd')
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstant_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_constant/constant_test_input.vhd')
        lExpected = [5,6,7,8,9,10]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcess_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_process/process_test_input.vhd')
        lExpected = [6,7,8,9,11,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42,46,47,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessBegin_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_process/process_test_input.vhd')
        lExpected = [6,13,20,28,34,40,47]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_process/process_test_input.vhd')
        lExpected = [6,11,17,24,32,38,46]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndProcess_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_process/process_test_input.vhd')
        lExpected = [9,15,22,30,36,42,48]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)




if __name__ == '__main__':
    unittest.main()
