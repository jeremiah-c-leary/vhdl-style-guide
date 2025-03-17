# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import assertion_statement as token
from vsg.vhdlFile.classify import assertion, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    assertion_statement ::=
        [ label : ] assertion ;
    """
    if utils.keyword_found("assert", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)

    iCurrent = assertion.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
