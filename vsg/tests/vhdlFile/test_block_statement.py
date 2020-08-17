import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','block_statement','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):

#    def test_tokens(self):
#        lExpected = []
#        lLine = []
#        lLine.append(token.entity.keyword)
#        lLine.append(parser.whitespace)
#        lExpected.append(lLine)
#
#        lActual = []
#        for oLine in oFile.get_lines():
#            lLine = []
#            for oObject in oLine.get_objects():
#                lLine.append(oObject)
#            lActual.append(lLine)
#
#        for iLine, lLine in enumerate(lExpected):
#            for oObject in oLine.get_objects():
#            self.assertEqual(type(l

    def test_classification(self):
        sTestDir = os.path.join(os.path.dirname(__file__),'..','block_statement')

        lExpected = []
        utils.read_file(os.path.join(sTestDir, 'classification_results.txt'), lExpected, False)

        lActual = []

        for oObject in utils.extract_objects(oFile, True):
            lActual.append(str(oObject))
        
        self.assertEqual(lExpected, lActual)

#    def test_debug(self):
#        utils.print_objects(oFile,True)
