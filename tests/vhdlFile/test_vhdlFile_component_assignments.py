
import unittest
from modules import vhdlFile

class testVhdlFileComponentAssignments(unittest.TestCase):


    def test_isComponent_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [5,16,27,36,45,56,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideComponent_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideComponent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isComponentEnd_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [12,23,34,43,52,65,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

#    def test_componentAlignmentColumn_assignment(self):
#        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
#        #lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
#        lExpected =  [ 6, 4, 6,11,10,10,10,10, 8,10,10, 9,10, 9, 8, 7, 8,10,12,13,10,15,14,10, 8,12,10, 8,11]
#        # Generic actual list
#        lActual = []
#        for iIndex, oLine in enumerate(oFile.lines):
#            if oLine.isComponent:
#                lActual.append(oLine.componentAlignmentColumn)
#        # Compare
#        self.assertEqual(lActual, lExpected)
# 
#    def test_componentIndentLevel_assignment(self):
#        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
#        #lExpected = [13,14,15,20,21,22,26,27,28,33,34,38,39,40,53,56,57,63,65,66,71,73,75,80,81,83,88,89,90]
#        lExpected =  [ 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 4, 5, 5, 4, 5, 5, 4, 4, 5, 4, 4, 4]
#        # Generic actual list
#        lActual = []
#        for iIndex, oLine in enumerate(oFile.lines):
#            if oLine.isComponent:
#                lActual.append(oLine.indentLevel)
#        # Compare
#        self.assertEqual(lActual, lExpected)

if __name__ == '__main__':
    unittest.main()
