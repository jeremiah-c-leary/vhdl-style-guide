import os

import unittest

from vsg.tests import utils
import vsg.vhdlFile as vhdlFile

sLrmUnit = utils.extract_lrm_unit_name(__name__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),sLrmUnit,'classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

    def test_classification(self):
        sTestDir = os.path.join(os.path.dirname(__file__),sLrmUnit)

        lExpected = []
        utils.read_file(os.path.join(sTestDir, 'classification_results.txt'), lExpected, False)

        lActual = []

        for oObject in utils.extract_objects(oFile, True):
            lActual.append(str(oObject))

        self.assertEqual(lExpected, lActual)
