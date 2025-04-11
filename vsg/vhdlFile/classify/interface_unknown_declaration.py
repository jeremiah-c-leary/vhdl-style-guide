# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_unknown_declaration as token
from vsg.vhdlFile.classify import expression, identifier_list, mode, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    This is a classification if the signal, constant, or variable keywords can not be found.
    This is not in the VHDL LRM.
    It is based off the interface_signal_declaration as it has the most keywords.

    interface_unknown_declaration ::=
        identifier_list : [ mode ] subtype_indication [ bus ] [ := *static*_expression ]
    """

    return not oDataStructure.is_next_token_one_of(["type", "file", "function", "procedure", "impure", "pure", "package"])


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    mode.classify(oDataStructure)

    subtype_indication.classify(oDataStructure)

    oDataStructure.replace_next_token_with_if("bus", token.bus_keyword)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_required(":=", token.assignment)

        expression.classify_until([";"], oDataStructure)
