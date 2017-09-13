
import unittest
from modules import vhdlFile

class testVhdlFileIfAssignments(unittest.TestCase):


    def test_isCaseKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_case/case_test_input.vhd')
        lExpected = [9,41]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseIsKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_case/case_test_input.vhd')
        lExpected = [9,43]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseIsKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseWhenKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_case/case_test_input.vhd')
        lExpected = [11,17,23,29,45,52,58,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndCaseKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_case/case_test_input.vhd')
        lExpected = [33,70]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndCaseKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideCaseWhen_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_case/case_test_input.vhd')
        lExpected = [11,17,23,29,45,46,52,58,59,60,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideCaseWhen:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isCaseWhenEnd_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_case/case_test_input.vhd')
        lExpected = [11,17,23,29,46,52,60,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)



if __name__ == '__main__':
    unittest.main()
