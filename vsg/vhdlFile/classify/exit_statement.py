# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import exit_statement as token
from vsg.vhdlFile.classify import condition, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    exit_statement ::=
        [ label : ] exit [ loop_label ] [ when condition ] ;
    """

    if utils.keyword_found("exit", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)

    iCurrent = utils.assign_next_token_required("exit", token.exit_keyword, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if_not_one_of([";", "when"], token.loop_label, iCurrent, lObjects)

    if utils.is_next_token("when", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("when", token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until([";"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
