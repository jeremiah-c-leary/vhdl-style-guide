
import unittest
from modules import vhdlFile

class testVhdlFileSequentialAssignments(unittest.TestCase):


    def test_isSequential_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_sequential/sequential_test_input.vhd')
        lExpected = [13,14,15,20,21,22,26,27,28,32,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideSequential_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_sequential/sequential_test_input.vhd')
        lExpected = [13,14,15,20,21,22,26,27,28,32,33,34,38,39,40,53,54,55,56,57,58,63,65,66,71,73,74,75,80,81,83,88,89,90]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideSequential:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSequentialEnd_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_sequential/sequential_test_input.vhd')
        lExpected = [13,14,15,20,21,22,26,27,28,32,33,34,38,39,40,55,56,58,63,65,66,71,74,75,80,81,83,88,89,90]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSequentialEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_sequentialAlignmentColumn_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_sequential/sequential_test_input.vhd')
        #lExpected = [13,14,15,20,21,22,26,27,28,32,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
        lExpected =  [ 6, 6, 6,10,10,10,10,10,10,10,10,10,10,10,10, 8, 8, 8,10,12,12,10,14,14,10,10,12,10,10,10]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                lActual.append(oLine.sequentialAlignmentColumn)
        # Compare
        self.assertEqual(lActual, lExpected)
 
    def test_sequentialIndentLevel_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_sequential/sequential_test_input.vhd')
        #lExpected = [13,14,15,20,21,22,26,27,28,32,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
        lExpected =  [ 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 4, 5, 5, 4, 5, 5, 4, 4, 5, 4, 4, 4]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isSequential:
                lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

if __name__ == '__main__':
    unittest.main()
