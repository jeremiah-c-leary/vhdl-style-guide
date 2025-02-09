# -*- coding: utf-8 -*-

from vsg.token import null_statement as token
from vsg.vhdlFile.classify import utils


def detect(oDataStructure):
    """
    null_statement ::=
        [ label : ] null ;
    """
    if utils.keyword_found("null", oDataStructure):
        classify(oDataStructure)
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required("null", token.null_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
