# -*- coding: utf-8 -*-

from vsg.token.psl import clock_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import utils as classify_utils


def detect(iToken, lObjects):
    """
    psl_clock_declaration ::=
        default clock DEF_SYM Clock_Expression ;
    """
    if utils.are_next_consecutive_tokens(["default", "clock"], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("default", token.default_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("clock", token.clock_keyword, iToken, lObjects)
    while not utils.is_next_token(";", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)
    return iCurrent
