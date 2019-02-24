import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','wait','wait_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile) 

class test_vhdlFile_wait_assignments(unittest.TestCase):

    def test_isWait(self):
        lExpected = [34,35,36]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isWait:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
