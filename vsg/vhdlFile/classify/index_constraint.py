# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import index_constraint as token
from vsg.vhdlFile.classify import discrete_range


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    index_constraint ::=
        ( discrete_range { , discrete_range } )
    """
 
    if oDataStructure.is_next_seek_token("("):
        oDataStructure.increment_seek_index()
        if discrete_range.detect(oDataStructure):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.open_parenthesis)

    while not oDataStructure.is_next_token(")"):
        discrete_range.classify_until([","], oDataStructure)
        oDataStructure.replace_next_token_with_if(",", token.comma)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
