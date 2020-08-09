import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import type_declaration as token
from vsg.token import access_type_definition
from vsg.token import record_type_definition
from vsg.token import element_declaration
from vsg.token import enumeration_type_definition
from vsg.token import constrained_array_definition
from vsg.token import range_constraint
from vsg.token import vhdl_range
from vsg.token import file_type_definition


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','type_declaration','classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class test_token(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((6,1))
        lExpected.append((9,1))
        lExpected.append((17,1))
        lExpected.append((20,1))
        lExpected.append((23,1))
        lExpected.append((26,1))
        lExpected.append((29,1))
        lExpected.append((32,1))

        utils.validate_token(self, oFile, lExpected, token.keyword)

    def test_identifier(self):
        lExpected = []
        lExpected.append((6,3))
        lExpected.append((9,3))
        lExpected.append((17,3))
        lExpected.append((20,3))
        lExpected.append((23,3))
        lExpected.append((26,3))
        lExpected.append((29,3))
        lExpected.append((32,3))


        utils.validate_token(self, oFile, lExpected, token.identifier)

    def test_is_keyword(self):
        lExpected = []
        lExpected.append((9,5))
        lExpected.append((17,5))
        lExpected.append((20,5))
        lExpected.append((23,5))
        lExpected.append((26,5))
        lExpected.append((29,5))
        lExpected.append((32,5))

        utils.validate_token(self, oFile, lExpected, token.is_keyword)


    def test_semicolon(self):
        lExpected = []
        lExpected.append((6,4))
        lExpected.append((14,6))
        lExpected.append((17,16))
        lExpected.append((20,28))
        lExpected.append((23,14))
        lExpected.append((26,16))
        lExpected.append((29,10))
        lExpected.append((32,12))

        utils.validate_token(self, oFile, lExpected, token.semicolon)


class test_access_type_definition_tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((29,7))

        utils.validate_token(self, oFile, lExpected, access_type_definition.keyword)


    def test_indication(self):
        lExpected = []
        lExpected.append((29,9))

        utils.validate_token(self, oFile, lExpected, access_type_definition.subtype_indication)


class test_record_type_definition_tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((9,7))

        utils.validate_token(self, oFile, lExpected, record_type_definition.keyword)

    def test_end_keyword(self):
        lExpected = []
        lExpected.append((14,1))

        utils.validate_token(self, oFile, lExpected, record_type_definition.end_keyword)

    def test_record_keyword(self):
        lExpected = []
        lExpected.append((14,3))

        utils.validate_token(self, oFile, lExpected, record_type_definition.record_keyword)

    def test_simple_name(self):
        lExpected = []
        lExpected.append((14,5))

        utils.validate_token(self, oFile, lExpected, record_type_definition.simple_name)


class test_element_declaration_tokens(unittest.TestCase):

    def test_identifier(self):
        lExpected = []
        lExpected.append((10,1))
        lExpected.append((11,1))
        lExpected.append((12,1))
        lExpected.append((13,1))

        utils.validate_token(self, oFile, lExpected, element_declaration.identifier)

    def test_colon(self):
        lExpected = []
        lExpected.append((10,3))
        lExpected.append((11,3))
        lExpected.append((12,3))
        lExpected.append((13,3))

        utils.validate_token(self, oFile, lExpected, element_declaration.colon)

    def test_subtype_definition(self):
        lExpected = []
        lExpected.append((10,5))
        lExpected.append((11,5))
        lExpected.append((12,5))
        lExpected.append((13,5))
        lExpected.append((13,6))
        lExpected.append((13,7))
        lExpected.append((13,9))
        lExpected.append((13,11))
        lExpected.append((13,12))

        utils.validate_token(self, oFile, lExpected, element_declaration.element_subtype_definition)

    def test_semi_colon(self):
        lExpected = []
        lExpected.append((10,6))
        lExpected.append((11,6))
        lExpected.append((12,6))
        lExpected.append((13,13))

        utils.validate_token(self, oFile, lExpected, element_declaration.semicolon)

class test_enumeration_type_definition_tokens(unittest.TestCase):

    def test_open_parenthesis(self):
        lExpected = []
        lExpected.append((17,7))

        utils.validate_token(self, oFile, lExpected, enumeration_type_definition.open_parenthesis)

    def test_enumeration_literal(self):
        lExpected = []
        lExpected.append((17,8))
        lExpected.append((17,11))
        lExpected.append((17,14))

        utils.validate_token(self, oFile, lExpected, enumeration_type_definition.enumeration_literal)

    def test_comma(self):
        lExpected = []
        lExpected.append((17,9))
        lExpected.append((17,12))

        utils.validate_token(self, oFile, lExpected, enumeration_type_definition.comma)

    def test_close_parenthesis(self):
        lExpected = []
        lExpected.append((17,15))

        utils.validate_token(self, oFile, lExpected, enumeration_type_definition.close_parenthesis)


class test_constrained_array_definition_tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((20,7))

        utils.validate_token(self, oFile, lExpected, constrained_array_definition.keyword)

    def test_index_constraint(self):
        lExpected = []
        lExpected.append((20,9))
        lExpected.append((20,10))
        lExpected.append((20,12))
        lExpected.append((20,14))
        lExpected.append((20,15))

        utils.validate_token(self, oFile, lExpected, constrained_array_definition.index_constraint)

    def test_of_keyword(self):
        lExpected = []
        lExpected.append((20,17))

        utils.validate_token(self, oFile, lExpected, constrained_array_definition.of_keyword)

    def test_element_subtype_indication(self):
        lExpected = []
        lExpected.append((20,19))
        lExpected.append((20,21))
        lExpected.append((20,23))
        lExpected.append((20,25))
        lExpected.append((20,27))

        utils.validate_token(self, oFile, lExpected, constrained_array_definition.subtype_indication)


class test_integer_and_float_type_tokens(unittest.TestCase):

    def test_range_constaint_keyword(self):
        lExpected = []
        lExpected.append((23,7))
        lExpected.append((26,7))

        utils.validate_token(self, oFile, lExpected, range_constraint.keyword)

    def test_vhdl_range(self):
        lExpected = []
        lExpected.append((23,9))
        lExpected.append((23,11))
        lExpected.append((23,13))

        lExpected.append((26,9))
        lExpected.append((26,10))
        lExpected.append((26,12))
        lExpected.append((26,14))
        lExpected.append((26,15))

        utils.validate_token(self, oFile, lExpected, vhdl_range.vhdl_range)


class test_access_type_definition_tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((29,7))

        utils.validate_token(self, oFile, lExpected, access_type_definition.keyword)

    def test_subtype_indication(self):
        lExpected = []
        lExpected.append((29,9))

        utils.validate_token(self, oFile, lExpected, access_type_definition.subtype_indication)


class test_file_type_definition_tokens(unittest.TestCase):

    def test_keyword(self):
        lExpected = []
        lExpected.append((32,7))

        utils.validate_token(self, oFile, lExpected, file_type_definition.keyword)

    def test_of_keyword(self):
        lExpected = []
        lExpected.append((32,9))

        utils.validate_token(self, oFile, lExpected, file_type_definition.of_keyword)

    def test_type_mark(self):
        lExpected = []
        lExpected.append((32,11))

        utils.validate_token(self, oFile, lExpected, file_type_definition.type_mark)
