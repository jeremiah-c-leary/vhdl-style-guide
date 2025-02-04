# -*- coding: utf-8 -*-

from vsg.token import context_reference as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import utils as classify_utils


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


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.keyword)
    classify_utils.classify_selected_name(oDataStructure, token)
    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_with(token.comma)
        classify_utils.classify_selected_name(oDataStructure, token)

    oDataStructure.replace_next_token_required(";", token.semicolon)
