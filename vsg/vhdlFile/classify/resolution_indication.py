# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import resolution_indication as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    resolution_indication ::=
        resolution_function_name | ( element_resolution )
    """

    if detect_element_resolution(oDataStructure):
        classify_element_resolution(oDataStructure)
        return True
    elif detect_resolution_function_name(oDataStructure):
        classify_resolution_function_name(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify_element_resolution(oDataStructure):
    oDataStructure.replace_next_token_required("(", token.open_parenthesis)
    utils.assign_tokens_until_matching_closing_paren(parser.todo, oDataStructure)
    oDataStructure.replace_next_token_required(")", token.close_parenthesis)


@decorators.print_classifier_debug_info(__name__)
def classify_resolution_function_name(oDataStructure):
    oDataStructure.replace_next_token_with(token.resolution_function_name)


@decorators.print_classifier_debug_info(__name__)
def detect_element_resolution(oDataStructure):
    # TODO:  Can this be is_next_token instead of is_next_seek_token?
    if oDataStructure.is_next_seek_token("("):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def detect_resolution_function_name(oDataStructure):
    return not detect_escape_value(oDataStructure)


lEscapeValues = ["(", ")", ";", ":=", "range", "bus", "is", "open", "'", ">>"]


@decorators.print_classifier_debug_info(__name__)
def detect_escape_value(oDataStructure):
    oDataStructure.increment_seek_index()
    return oDataStructure.is_next_seek_token_one_of(lEscapeValues)
