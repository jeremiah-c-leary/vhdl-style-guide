# -*- coding: utf-8 -*-

from vsg.token import constant_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, identifier_list, subtype_indication


def detect(oDataStructure):
    """
    constant_declaration ::=
        constant identifier_list : subtype_indication [ := expression ] ;
    """

    if oDataStructure.is_next_token("constant"):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.constant_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_with(token.assignment_operator)

        expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
