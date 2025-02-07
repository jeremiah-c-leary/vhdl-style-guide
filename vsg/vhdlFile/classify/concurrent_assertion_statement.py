# -*- coding: utf-8 -*-

from vsg.token import concurrent_assertion_statement as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import assertion


def detect(oDataStructure):
    """
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;

    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    """

    if oDataStructure.exists_in_next_n_tokens("assert", 4):
        classify(oDataStructure)
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.label_name, token.label_colon)

    iCurrent = utils.assign_next_token_if("postponed", token.postponed_keyword, iCurrent, lObjects)

    iCurrent = assertion.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
