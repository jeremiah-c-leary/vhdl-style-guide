# -*- coding: utf-8 -*-

from vsg.token import return_statement as token
from vsg.vhdlFile.classify import expression, utils


def detect(oDataStructure):
    """
    return_statement ::=
        [ label : ] return [ expression ] ;
    """

    if utils.keyword_found("return", oDataStructure):
        classify(oDataStructure)
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required("return", token.return_keyword, iCurrent, lObjects)
    if not utils.is_next_token(";", iCurrent, lObjects):
        iCurrent = expression.classify_until([";"], iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
