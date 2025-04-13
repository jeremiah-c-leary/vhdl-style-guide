# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import use_clause as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    use_clause ::=
        use selected_name { , selected_name } ;
    """
    if oDataStructure.is_next_token("use"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_current_token_with(token.keyword)

    while not oDataStructure.is_next_token(";"):
        utils.classify_selected_name(oDataStructure, token)
        oDataStructure.replace_next_token_with_if(",", token.comma)

    oDataStructure.replace_next_token_required(";", token.semicolon)
