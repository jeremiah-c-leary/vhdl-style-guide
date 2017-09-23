
import unittest
from modules import vhdlFile

class testVhdlFileInstantiationAssignments(unittest.TestCase):


    def test_isInstantiation_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_instantiation/instantiation_test_input.vhd')
        lExpected = [6,17,23,29,36,44,52]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideInstantiation_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_instantiation/instantiation_test_input.vhd')
        lExpected = [6,7,8,9,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,52,53,54,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideInstantiation:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationPortKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_instantiation/instantiation_test_input.vhd')
        lExpected = [7,18,24,31,37,45,52]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationPortEnd_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_instantiation/instantiation_test_input.vhd')
        lExpected = [11,22,28,35,42,50,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isInstantiationPortAssignment_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_instantiation/instantiation_test_input.vhd')
        lExpected = [8,9,10,19,20,21,25,26,27,32,33,34,39,40,41,46,47,48,53,54,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

if __name__ == '__main__':
    unittest.main()
