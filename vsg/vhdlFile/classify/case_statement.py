# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import case_statement as token
from vsg.vhdlFile.classify import case_statement_alternative, expression, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    case_statement ::=
        [ *case*_label : ]
            case [ ? ] expression is
                case_statement_alternative
                { case_statement_alternative }
        end case [ ? ] [ case_label ] ;
    """
    if utils.keyword_found("case", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.case_label, token.label_colon)
    oDataStructure.replace_next_token_required("case", token.case_keyword)
    oDataStructure.replace_next_token_with_if("?", token.question_mark)

    expression.classify_until(["is"], oDataStructure)

    oDataStructure.replace_next_token_required("is", token.is_keyword)

    while case_statement_alternative.detect(oDataStructure):
        pass

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("case", token.end_case_keyword)
    oDataStructure.replace_next_token_with_if("?", token.question_mark)
    oDataStructure.replace_next_token_with_if_not(";", token.end_case_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)
