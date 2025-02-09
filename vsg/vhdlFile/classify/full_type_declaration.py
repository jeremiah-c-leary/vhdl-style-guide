# -*- coding: utf-8 -*-

from vsg.token import full_type_declaration as token
from vsg.vhdlFile.classify import identifier, type_definition


def detect(oDataStructure):
    """
    full_type_declaration ::=
        type identifier is type_definition ;
    """

    if oDataStructure.are_next_consecutive_tokens(["type", None, "is"]):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.type_keyword)

    identifier.classify(oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required("is", token.is_keyword)

    type_definition.detect(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
