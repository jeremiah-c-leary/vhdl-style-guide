# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import constant_declaration as token
from vsg.vhdlFile.classify import expression, identifier_list, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    constant_declaration ::=
        constant identifier_list : subtype_indication [ := expression ] ;
    """

    if oDataStructure.is_next_token("constant"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.constant_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_with(token.assignment_operator)

        expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
