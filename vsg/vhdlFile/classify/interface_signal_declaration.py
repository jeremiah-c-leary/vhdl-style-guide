# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_signal_declaration as token
from vsg.vhdlFile.classify import expression, identifier_list, mode, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_signal_declaration ::=
        [ signal ] identifier_list : [ mode ] subtype_indication [ bus ] [ := *static*_expression ]
    """

    return oDataStructure.is_next_token("signal")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.signal_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    mode.classify(oDataStructure)

    subtype_indication.classify(oDataStructure)

    oDataStructure.replace_next_token_with_if("bus", token.bus_keyword)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_with(token.assignment)

        expression.classify_until([";"], oDataStructure)
