# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import array_constraint as token
from vsg.vhdlFile.classify import array_element_constraint, index_constraint


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    array_constraint ::=
        index_constraint [ array_element_constraint ]
      | ( open ) [ array_element_constraint ]

    """

    if open_detected(oDataStructure):
        classify_open(oDataStructure)
        array_element_constraint.detect(oDataStructure)
        return True

    if index_constraint.detect(oDataStructure):
        index_constraint.classify(oDataStructure)
        array_element_constraint.detect(oDataStructure)
        return True

    return False


@decorators.print_classifier_debug_info(__name__)
def detect_discrete_subtype_indication(oDataStructure):
    if oDataStructure.is_next_seek_token("("):
        index_constraint.classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def open_detected(oDataStructure):
    return oDataStructure.are_next_consecutive_tokens(["(", "open"])


@decorators.print_classifier_debug_info(__name__)
def classify_open(oDataStructure):
    oDataStructure.replace_next_token_with(token.open_parenthesis)
    oDataStructure.replace_next_token_with(token.open_keyword)
    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
