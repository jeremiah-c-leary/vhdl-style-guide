# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_assertion_statement as token
from vsg.vhdlFile.classify import assertion, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;

    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    """

    if (
        oDataStructure.are_next_consecutive_tokens([None, ":", "postponed", "assert"])
        or oDataStructure.are_next_consecutive_tokens([None, ":", "assert"])
        or oDataStructure.are_next_consecutive_tokens(["postponed", "assert"])
        or oDataStructure.is_next_token("assert")
    ):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)

    oDataStructure.replace_next_token_with_if("postponed", token.postponed_keyword)

    assertion.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
