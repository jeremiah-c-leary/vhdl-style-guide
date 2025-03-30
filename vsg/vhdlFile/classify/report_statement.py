# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import report_statement as token
from vsg.vhdlFile.classify import expression, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    report_statement ::=
        [ label : ]
            report expression
                [ severity expression ] ;
    """

    if utils.keyword_found("report", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)
    oDataStructure.replace_next_token_with(token.report_keyword)

    expression.classify_until([";", "severity"], oDataStructure)

    if oDataStructure.is_next_token("severity"):
        oDataStructure.replace_next_token_with(token.severity_keyword)
        expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
