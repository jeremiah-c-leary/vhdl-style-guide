# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import association_element as token
from vsg.vhdlFile.classify import formal_part


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    association_element ::=
        [ formal_part => ] actual_part

    An association element will either end in a close parenthesis or a comma that is not within parenthesis.

    association_element [)|,]

    """
    iParen = 1
    while not oDataStructure.is_next_seek_token(";"):
        oDataStructure.advance_to_next_seek_token()
        if oDataStructure.seek_token_lower_value_is("("):
            iParen += 1
        elif oDataStructure.seek_token_lower_value_is(")"):
            if iParen == 1:
                classify(oDataStructure)
                return True
            iParen -= 1
        if iParen == 1:
            if oDataStructure.seek_token_lower_value_is(","):
                classify(oDataStructure)
                return True
        oDataStructure.increment_seek_index()
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.set_mark_index()

    classify_formal_part(oDataStructure)
    classify_actual_part(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify_formal_part(oDataStructure):
    if oDataStructure.does_string_exist_before_mark_index_honoring_parenthesis_hierarchy("=>"):
        formal_part.classify(oDataStructure, token.formal_part)
        oDataStructure.replace_next_token_with(token.assignment)


@decorators.print_classifier_debug_info(__name__)
def classify_actual_part(oDataStructure):
    oDataStructure.replace_tokens_from_current_to_mark_with(token.actual_part)
