# -*- coding: utf-8 -*-

from vsg.token import use_clause as token
from vsg.vhdlFile.classify import utils


def detect(oDataStructure):
    """
    use_clause ::=
        use selected_name { , selected_name } ;
    """
    if oDataStructure.is_next_token("use"):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.assign_next_token_required("use", token.keyword)

    while not oDataStructure.is_next_token(";"):
        utils.classify_selected_name(oDataStructure, token)
        oDataStructure.replace_next_token_with_if(",", token.comma)

    oDataStructure.assign_next_token_required(";", token.semicolon)
