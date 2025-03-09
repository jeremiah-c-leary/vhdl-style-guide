# -*- coding: utf-8 -*-

from vsg.token.psl import sequence_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import utils as classify_utils


def detect(iToken, lObjects):
    """
    psl_sequence_declaration ::=
        sequence PSL_Identifier [ ( Formal_Parameter_List ) ] DEF_SYM Sequence ;
    """
    if utils.is_next_token("sequence", iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("sequence", token.sequence_keyword, iToken, lObjects)
    while not utils.is_next_token(";", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)
    return iCurrent
