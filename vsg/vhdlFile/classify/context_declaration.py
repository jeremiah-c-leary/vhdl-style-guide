# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import context_declaration as token
from vsg.vhdlFile.classify import context_clause


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    context_declaration ::=
        context identifier is
            context_clause
        end [ context ] [ context_simple_name ] ;
    """

    if oDataStructure.is_next_token("context"):
        if oDataStructure.does_string_exist_before_string("is", ";"):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_current_token_with(token.context_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("is", token.is_keyword)

    context_clause.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_with_if("context", token.end_context_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.context_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
