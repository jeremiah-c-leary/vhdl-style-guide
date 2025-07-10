# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import for_generate_statement as token
from vsg.vhdlFile.classify import (
    generate_statement_body,
    parameter_specification,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    for_generate_statement ::=
        *generate*_label :
            for *generate*_parameter_specification generate
                generate_statement_body
            end generate [ *generate*_label ] ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "for"]):
        classify(oDataStructure)
        return True
    if oDataStructure.is_next_token("for"):
        iIndex = utils.find_next_token(iCurrent, lObjects)
        oToken = token.for_keyword(lObjects[iCurrent].get_value())
        utils.print_error_message("generate_label", oToken, iIndex, lObjects)
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.generate_label, token.label_colon)

    oDataStructure.replace_next_token_required("for", token.for_keyword)

    parameter_specification.classify_until(["generate"], oDataStructure)

    oDataStructure.replace_next_token_required("generate", token.generate_keyword)

    generate_statement_body.classify(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("generate", token.end_generate_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_generate_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)
