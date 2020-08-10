import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import procedure_specification as token
from vsg.token import subprogram_declaration
from vsg.token import subprogram_header
from vsg.token import generic_map_aspect
from vsg.token import association_list
from vsg.token import association_element


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','procedure_specification','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_token(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((10,1))
        lExpected.append((12,1))
        lExpected.append((14,1))
        lExpected.append((19,1))
        lExpected.append((22,1))
        lExpected.append((27,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)

    def test_designator(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((10,3))
        lExpected.append((12,3))
        lExpected.append((14,3))
        lExpected.append((19,3))
        lExpected.append((22,3))
        lExpected.append((27,3))

        utils.validate_token(self, oFile, lExpected, token.designator)

    def test_open_parenthesis(self):
        lExpected = []
        lExpected.append((7,1))
        lExpected.append((10,5))
        lExpected.append((12,5))
        lExpected.append((14,4))
        lExpected.append((19,7))
        lExpected.append((24,3))
        lExpected.append((31,3))

        utils.validate_token(self, oFile, lExpected, token.open_parenthesis)

    def test_close_parenthesis(self):
        lExpected = []
        lExpected.append((8,10))
        lExpected.append((10,24))
        lExpected.append((12,14))
        lExpected.append((16,18))
        lExpected.append((19,16))
        lExpected.append((24,12))
        lExpected.append((31,12))

        utils.validate_token(self, oFile, lExpected, token.close_parenthesis)

    def test_parameter(self):
        lExpected = []
        lExpected.append((19,5))
        lExpected.append((24,1))
        lExpected.append((31,1))

        utils.validate_token(self, oFile, lExpected, token.parameter_keyword)

    def test_semicolon(self):
        lExpected = []
        lExpected.append((8,11))
        lExpected.append((10,25))
        lExpected.append((12,15))
        lExpected.append((16,19))
        lExpected.append((19,17))
        lExpected.append((24,13))
        lExpected.append((31,13))

        utils.validate_token(self, oFile, lExpected, subprogram_declaration.semicolon)

    def test_subprogram_header_keyword(self):
        lExpected = []
        lExpected.append((23,1))
        lExpected.append((28,1))

        utils.validate_token(self, oFile, lExpected, subprogram_header.keyword)


    def test_subprogram_header_open_parenthesis(self):
        lExpected = []
        lExpected.append((23,3))
        lExpected.append((28,3))

        utils.validate_token(self, oFile, lExpected, subprogram_header.open_parenthesis)

    def test_subprogram_header_close_parenthesis(self):
        lExpected = []
        lExpected.append((23,33))
        lExpected.append((28,33))

        utils.validate_token(self, oFile, lExpected, subprogram_header.close_parenthesis)

    def test_generic_map_aspect_keyword(self):
        lExpected = []
        lExpected.append((29,1))

        utils.validate_token(self, oFile, lExpected, generic_map_aspect.keyword)

    def test_generic_map_aspect_map_keyword(self):
        lExpected = []
        lExpected.append((29,3))

        utils.validate_token(self, oFile, lExpected, generic_map_aspect.map_keyword)

    def test_generic_map_aspect_open_parenthesis(self):
        lExpected = []
        lExpected.append((29,5))

        utils.validate_token(self, oFile, lExpected, generic_map_aspect.open_parenthesis)

    def test_generic_map_aspect_close_parenthesis(self):
        lExpected = []
        lExpected.append((30,6))

        utils.validate_token(self, oFile, lExpected, generic_map_aspect.close_parenthesis)

    def test_association_list_comma(self):
        lExpected = []
        lExpected.append((29,11))
        lExpected.append((29,19))

        utils.validate_token(self, oFile, lExpected, association_list.comma)

    def test_association_element_assignment(self):
        lExpected = []
        lExpected.append((29,8))
        lExpected.append((29,15))
        lExpected.append((30,3))

        utils.validate_token(self, oFile, lExpected, association_element.assignment)

    def test_association_element_formal_part(self):
        lExpected = []
        lExpected.append((29,6))
        lExpected.append((29,13))
        lExpected.append((30,1))

        utils.validate_token(self, oFile, lExpected, association_element.formal_part)

    def test_association_element_actual_part(self):
        lExpected = []
        lExpected.append((29,10))
        lExpected.append((29,17))
        lExpected.append((29,18))
        lExpected.append((30,5))

        utils.validate_token(self, oFile, lExpected, association_element.actual_part)

#    def test_print_objects(self):
#        utils.print_objects(oFile, True)

