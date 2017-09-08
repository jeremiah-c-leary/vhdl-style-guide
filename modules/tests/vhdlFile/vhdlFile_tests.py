
import sys
sys.path.append('..\..')
import unittest
import vhdlFile

class testVhdlFileMethods(unittest.TestCase):

    def test_vhdlFile_class_exists(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')
        self.assertTrue(oFile)
        self.assertEqual(oFile.filename, '../rule_library/library_test_input.vhd')

    def test_loading_of_file(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')

        # Read in test file used for all tests
        lExpected = ['']
        with open('../rule_library/library_test_input.vhd') as oExpectedFile:
            for sLine in oExpectedFile:
                lExpected.append(sLine.rstrip())
        oExpectedFile.close()
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            self.assertEqual(oLine.line, lExpected[iIndex])

    def test_blank_line_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')

        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == 1 or iIndex == 2 or iIndex == 6 or iIndex == 8 or iIndex == 11 or \
               iIndex == 12 or iIndex == 15 or iIndex == 17 or iIndex == 18 or iIndex == 19 or \
               iIndex == 22 or iIndex == 25 or iIndex == 28 or iIndex == 30:
                self.assertTrue(oLine.isBlank)
            else:
                self.assertFalse(oLine.isBlank)

    def test_library_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')
        lExpected = [3,7,9,13,20,21]
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibrary)
                self.assertEqual(oLine.indentLevel, 0)
            else:
                self.assertFalse(oLine.isLibrary)

    def test_library_use_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')
        lExpected = [4,5,10,14,16,23,24,26,27,29]
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibraryUse)
                self.assertEqual(oLine.indentLevel, 1)
            else:
                self.assertFalse(oLine.isLibraryUse)


if __name__ == '__main__':
    unittest.main()
