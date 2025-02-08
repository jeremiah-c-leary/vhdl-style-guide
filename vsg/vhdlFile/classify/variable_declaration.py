# -*- coding: utf-8 -*-

from vsg.token import variable_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, identifier_list, subtype_indication


def detect(oDataStructure):
    """
    variable_declaration ::=
        [ shared ] variable identifier_list : subtype_indication [ := expression ] ;
    """

    if oDataStructure.is_next_token_one_of(["shared", "variable"]):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("shared", token.shared_keyword)
    oDataStructure.replace_next_token_required("variable", token.variable_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_with(token.assignment_operator)
        expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
