# -*- coding: utf-8 -*-

from vsg.token import report_statement as token
from vsg.vhdlFile.classify import expression, utils
from vsg import decorators


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
def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required("report", token.report_keyword, iCurrent, lObjects)

    iCurrent = expression.classify_until([";", "severity"], iCurrent, lObjects)

    if utils.is_next_token("severity", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("severity", token.severity_keyword, iCurrent, lObjects)
        iCurrent = expression.classify_until([";"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
