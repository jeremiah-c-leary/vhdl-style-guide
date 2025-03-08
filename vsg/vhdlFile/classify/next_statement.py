# -*- coding: utf-8 -*-

from vsg.token import next_statement as token
from vsg.vhdlFile.classify import condition, utils
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    next_statement ::=
        [ label : ] next [ loop_label ] [ when condition ] ;
    """
    if utils.keyword_found("next", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required("next", token.next_keyword, iCurrent, lObjects)

    if not utils.is_next_token(";", iCurrent, lObjects) and not utils.is_next_token("when", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.loop_label, iCurrent, lObjects)

    if utils.is_next_token("when", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("when", token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until([";"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
