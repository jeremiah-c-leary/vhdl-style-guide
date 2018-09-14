import os

import unittest
from vsg import vhdlFile

oFileBlock = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','block','block_test_input.vhd'))

class testVhdlFileMethods(unittest.TestCase):

    def test_insideBlock_assignment(self):
        lExpected = range(10,29)
        lActual = [i for i, l in enumerate(oFileBlock.lines) if l.insideBlock]
        self.assertEqual(lActual, lExpected)

    def test_isBlockBegin_assignment(self):
        lExpected = [18]
        lActual = [i for i, l in enumerate(oFileBlock.lines) if l.isBlockBegin]
        self.assertEqual(lActual, lExpected)

    def test_isBlockKeyword_assignment(self):
        lExpected = [10]
        lActual = [i for i, l in enumerate(oFileBlock.lines) if l.isBlockKeyword]
        self.assertEqual(lActual, lExpected)

    def test_isEndBlock_assignment(self):
        lExpected = [28]
        lActual = [i for i, l in enumerate(oFileBlock.lines) if l.isEndBlock]
        self.assertEqual(lActual, lExpected)

    def test_block_indent_assignment(self):
#       lExpected = [   0,   1,2,3,   4,5,   6,7,   8,9,10,11,  12,13,  14,15,16,17,18,19,  20,21,22,23,24,25,26,  27,28,  29,30,  31]
        lExpected = [None,None,0,0,None,0,None,0,None,1, 1, 2,None, 2,None, 2, 3, 2, 1, 2,None, 2, 3, 4, 4, 4, 3,None, 1,None, 0,None]
        lActual = [oLine.indentLevel for oLine in oFileBlock.lines]
        self.assertEqual(lActual, lExpected)

    def test_isInstance_assignment(self):
        lExpected = [21]
        lActual = [i for i, l in enumerate(oFileBlock.lines) if l.isInstantiationDeclaration]
        self.assertEqual(lActual, lExpected)

