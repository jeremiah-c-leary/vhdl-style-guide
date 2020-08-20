import os

import unittest

from vsg.vhdlFile import vhdlFile_new
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','block_statement','classification_test_input.vhd'))
oFile = vhdlFile_new.vhdlFile(lFile)


class test_token(unittest.TestCase):


    def test_classification(self):
        sTestDir = os.path.join(os.path.dirname(__file__),'..','block_statement')

        lExpected = []
        utils.read_file(os.path.join(sTestDir, 'classification_results.txt'), lExpected, False)

        lActual = []

        for oObject in utils.extract_objects(oFile, True):
            lActual.append(str(oObject))
        
        self.assertEqual(lExpected, lActual)

    def test_debug(self):
        utils.print_objects(oFile, True)
