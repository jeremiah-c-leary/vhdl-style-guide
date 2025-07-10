# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import context_reference as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    context_reference ::=
        context selected_name { , selected_name } ;
    """
    if oDataStructure.is_next_token("context"):
        if not oDataStructure.does_string_exist_before_string("is", ";"):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_current_token_with(token.keyword)
    utils.classify_selected_name(oDataStructure, token)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_current_token_with(token.comma)
        utils.classify_selected_name(oDataStructure, token)

    oDataStructure.replace_next_token_required(";", token.semicolon)
