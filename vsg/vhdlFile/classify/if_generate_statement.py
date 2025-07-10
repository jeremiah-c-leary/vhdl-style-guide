# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import if_generate_statement as token
from vsg.vhdlFile.classify import condition, generate_statement_body, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    if_generate_statement ::=
        *generate*_label :
            if [ *alternative*_label : ] condition generate
                generate_statement_body
            { elsif [ *alternative_label* : ] condition generate
                generate_statement_body }
            [ else [ *alternative_label* : ] generate
                generate_statement_body ]
            end generate [ *generate*_label ] ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "if"]):
        classify(oDataStructure)
        return True
    if oDataStructure.is_next_token("if"):
        iIndex = utils.find_next_token(iCurrent, lObjects)
        oToken = token.if_keyword(lObjects[iCurrent].get_value())
        utils.print_error_message("generate_label", oToken, iIndex, lObjects)
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.generate_label, token.label_colon)

    classify_if(oDataStructure)

    while oDataStructure.is_next_token("elsif"):
        classify_elsif(oDataStructure)

    if oDataStructure.is_next_token("else"):
        classify_else(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("generate", token.end_generate_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_generate_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)


def classify_if(oDataStructure):
    oDataStructure.replace_next_token_required("if", token.if_keyword)

    classify_line(oDataStructure)


def classify_elsif(oDataStructure):
    oDataStructure.replace_next_token_required("elsif", token.elsif_keyword)

    classify_line(oDataStructure)


def classify_else(oDataStructure):
    oDataStructure.replace_next_token_required("else", token.else_keyword)

    classify_line(oDataStructure)


def classify_line(oDataStructure):
    classify_alternative_label(oDataStructure)

    condition.classify_until(["generate"], oDataStructure)

    oDataStructure.replace_next_token_required("generate", token.generate_keyword)

    generate_statement_body.classify(oDataStructure)


def classify_alternative_label(oDataStructure):
    if oDataStructure.are_next_consecutive_tokens([None, ":"]):
        oDataStructure.replace_next_token_with(token.alternative_label_name)
        oDataStructure.replace_next_token_with(token.alternative_label_colon)
