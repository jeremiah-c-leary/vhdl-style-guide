# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import wait_statement as token
from vsg.vhdlFile.classify import (
    condition_clause,
    sensitivity_clause,
    timeout_clause,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    wait_statement ::=
        [ label : ] wait [ sensitivity_clause ] [ condition_clause ] [ timeout_clause ] ;
    """
    if utils.keyword_found("wait", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)
    oDataStructure.replace_next_token_with(token.wait_keyword)

    if sensitivity_clause.detect(oDataStructure):
        sensitivity_clause.classify_until([";", "for", "until"], oDataStructure)

    if condition_clause.detect(oDataStructure):
        condition_clause.classify_until([";", "for"], oDataStructure)

    if timeout_clause.detect(oDataStructure):
        timeout_clause.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
