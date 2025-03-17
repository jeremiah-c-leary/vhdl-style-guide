# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import signal_declaration as token
from vsg.vhdlFile.classify import (
    expression,
    identifier_list,
    signal_kind,
    subtype_indication,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    signal_declaration ::=
        signal identifier_list : subtype_indication [ signal_kind ] [ := expression ] ;
    """

    if oDataStructure.is_next_token("signal"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.signal_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)

    signal_kind.detect(oDataStructure)

    if oDataStructure.is_next_token(":="):
        oDataStructure.replace_next_token_with(token.assignment_operator)
        expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
