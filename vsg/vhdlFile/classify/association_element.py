# -*- coding: utf-8 -*-

from vsg.token import association_element as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import formal_part


def detect(oDataStructure):
    """
    association_element ::=
        [ formal_part => ] actual_part

    An association element will either end in a close parenthesis or a comma that is not within parenthesis.

    association_element [)|,]

    """
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    oDataStructure.align_seek_index()
    while not oDataStructure.is_next_seek_token(";"):
        oDataStructure.advance_to_next_seek_token()
        if oDataStructure.seek_token_lower_value_is("("):
            iOpenParenthesis += 1
        if oDataStructure.seek_token_lower_value_is(")"):
            iCloseParenthesis += 1
        if iCloseParenthesis == iOpenParenthesis + 1:
            classify(oDataStructure, ")")
            return True
        if iCloseParenthesis == iOpenParenthesis:
            if oDataStructure.seek_token_lower_value_is(","):
                classify(oDataStructure, ",")
                return True
        oDataStructure.increment_seek_index()
    return False


def classify(oDataStructure, sEnd):
    # Classify formal part if it exists
    if formal_part_detected(oDataStructure):
        formal_part.classify(oDataStructure, token.formal_part)
        oDataStructure.replace_next_token_with(token.assignment)

    # Classify actual part
    oDataStructure.replace_tokens_from_current_to_seek_with(token.actual_part)


def formal_part_detected(oDataStructure):
    iParen = 0
    for iIndex in range(oDataStructure.get_current_index(), oDataStructure.get_seek_index()):
        iParen = utils.update_paren_counter(iIndex, oDataStructure.lAllObjects, iParen)
        if iParen == 0 and utils.object_value_is(oDataStructure.lAllObjects, iIndex, "=>"):
            return True
    return False
