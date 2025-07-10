# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import case_generate_statement as token
from vsg.vhdlFile.classify import case_generate_alternative, expression, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    case_generate_statement ::=
        *generate*_label :
            case expression generate
                case_generate_alternative
                { case_generate_alternative }
            end generate [ *generate*_label ] ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "case"]):
        classify(oDataStructure)
        return True
    if oDataStructure.is_next_token("case"):
        iIndex = utils.find_next_token(iToken, lObjects)
        oToken = token.case_keyword(lObjects[iToken].get_value())
        utils.print_error_message("generate_label", oToken, iIndex, lObjects)
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.generate_label, token.label_colon)

    oDataStructure.replace_next_token_required("case", token.case_keyword)

    expression.classify_until(["generate"], oDataStructure)

    oDataStructure.replace_next_token_required("generate", token.generate_keyword)

    while case_generate_alternative.detect(oDataStructure):
        pass

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("generate", token.end_generate_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_generate_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)
