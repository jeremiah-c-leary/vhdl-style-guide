# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subprogram_header as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import generic_list, generic_map_aspect


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_header ::=
        [ generic ( generic_list )
        [ generic_map_aspect ] ]
    """

    if oDataStructure.is_next_token("generic"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if oDataStructure.does_string_exist_in_next_n_tokens("(", 2):
        oDataStructure.replace_next_token_required("generic", token.generic_keyword)
        oDataStructure.replace_next_token_required("(", token.open_parenthesis)

        generic_list.classify(oDataStructure)

        oDataStructure.replace_next_token_required(")", token.close_parenthesis)

    generic_map_aspect.detect(oDataStructure)
