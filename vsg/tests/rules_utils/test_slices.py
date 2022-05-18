
import os
import unittest

from vsg.rules import utils as rules_utils
from vsg import vhdlFile
from vsg.tests import utils

from vsg import parser
from vsg import token


sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'combine_slices.vhd'))


class test_function(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_extract_slice_indexes(self):
        lActual = rules_utils.extract_slice_indexes(self.oFile.lAllObjects)

        lExpected = []
        lExpected.append([23, 33])
        lExpected.append([38, 46])
        lExpected.append([49, 59])
        lExpected.append([64, 72])
        lExpected.append([89, 97])
        lExpected.append([102, 110])
        lExpected.append([113, 121])
        lExpected.append([126, 134])
        lExpected.append([151, 159])
        lExpected.append([160, 168])
        lExpected.append([169, 177])
        lExpected.append([178, 186])

        self.assertEqual(lExpected, lActual)


    def test_combine_slice_indexes(self):
        lActual = rules_utils.combine_slice_indexes(self.oFile.lAllObjects)
        
        lExpected = []

        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(token.architecture_body.architecture_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.architecture_body.identifier)
        lExpected.append(parser.whitespace)
        lExpected.append(token.architecture_body.of_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.architecture_body.entity_name)
        lExpected.append(parser.whitespace)
        lExpected.append(token.architecture_body.is_keyword)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.signal_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.identifier)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.colon)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.open_parenthesis)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.comma)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.open_parenthesis)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.close_parenthesis)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.close_parenthesis)
        lExpected.append(token.signal_declaration.semicolon)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.signal_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.identifier)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.colon)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.open_parenthesis)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.comma)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.open_parenthesis)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.close_parenthesis)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.close_parenthesis)
        lExpected.append(token.signal_declaration.semicolon)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.signal_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.identifier)
        lExpected.append(parser.whitespace)
        lExpected.append(token.signal_declaration.colon)
        lExpected.append(parser.whitespace)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.open_parenthesis)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.comma)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.open_parenthesis)
        lExpected.append(parser.slice_name)
        lExpected.append(parser.close_parenthesis)
        lExpected.append(parser.close_parenthesis)
        lExpected.append(token.signal_declaration.semicolon)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(token.architecture_body.begin_keyword)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)
        lExpected.append(token.architecture_body.end_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.architecture_body.end_architecture_keyword)
        lExpected.append(parser.whitespace)
        lExpected.append(token.architecture_body.architecture_simple_name)
        lExpected.append(token.architecture_body.semicolon)
        lExpected.append(parser.carriage_return)
        lExpected.append(parser.blank_line)
        lExpected.append(parser.carriage_return)


        for i in range(0, len(lExpected)):
#            print(f'{lExpected[i]} | {lActual[i]}')
            self.assertTrue(isinstance(lActual[i], lExpected[i]))

        self.assertEqual(len(lExpected), len(lActual))

