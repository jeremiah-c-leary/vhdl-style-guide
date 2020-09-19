import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils
from vsg.token import attribute_declaration

lFileAttribute = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','attribute','attribute_test_input.vhd'))
oFileAttribute = vhdlFile.vhdlFile(lFileAttribute)

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','attribute','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileAttributeAttributeMethods(unittest.TestCase):

    def test_isAttributeKeyword_assignment(self):
        lExpected = [4,5,9,11]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileAttribute.lines):
            if oLine.isAttributeKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isAttributeEnd_assignment(self):
        lExpected = [4,6,9,12]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileAttribute.lines):
            if oLine.isAttributeEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideAttribute_assignment(self):
        lExpected = [4,5,6,9,11,12]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileAttribute.lines):
            if oLine.insideAttribute:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
