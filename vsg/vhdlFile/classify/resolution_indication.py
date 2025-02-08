# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import resolution_indication as token
from vsg.vhdlFile import utils


def detect(oDataStructure):
    """
    resolution_indication ::=
        resolution_function_name | ( element_resolution )
    """
    oDataStructure.advance_seek_index_to_current_index()
    if detect_element_resolution(oDataStructure):
        classify_element_resolution(oDataStructure)
        return True
    elif detect_resolution_function_name(oDataStructure):
        classify_resolution_function_name(oDataStructure)
        return True
    oDataStructure.align_seek_index()
    return False


def classify_element_resolution(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iToken, lObjects)
    iCurrent = utils.assign_tokens_until_matching_closing_paren(parser.todo, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    return iCurrent


def classify_resolution_function_name(iToken, lObjects):
    return utils.assign_next_token(token.resolution_function_name, iToken, lObjects)


def detect_element_resolution(oDataStructure):
    if oDataStructure.is_next_seek_token("("):
        return True
    return False


def detect_resolution_function_name(oDataStructure):
    return not detect_escape_value(oDataStructure)


lEscapeValues = ["(", ")", ";", ":=", "range", "bus", "is", "open", "'", ">>"]


def detect_escape_value(oDataStructure):
    oDataStructure.increment_seek_index()
    return oDataStructure.is_next_seek_token_one_of(lEscapeValues)
