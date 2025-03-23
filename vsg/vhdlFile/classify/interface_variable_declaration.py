# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_variable_declaration as token
from vsg.vhdlFile.classify import expression, identifier_list, mode, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_variable_declaration ::=
    [ variable ] identifier_list : [ mode ] subtype_indication [ := static_expression ]
    """

    return oDataStructure.is_next_token("variable")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.variable_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    mode.classify(oDataStructure)

    subtype_indication.classify(oDataStructure)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_with(token.assignment)
        expression.classify_until([";"], oDataStructure)
