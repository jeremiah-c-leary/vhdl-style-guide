# -*- coding: utf-8 -*-

from vsg.token.psl import assert_directive as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    [ label : ] Assert_Directive

    Assert_Directive ::=
        assert Property [ report String ] ;
    """

    if utils.are_next_consecutive_tokens([None, ":", "assert"], iToken, lObjects) or utils.is_next_token("assert", iToken, lObjects):
        if utils.find_in_range("[", iToken, ";", lObjects) and utils.find_in_range("report", iToken, ";", lObjects):
            return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("assert", token.assert_keyword, iToken, lObjects)
    iCurrent = utils.assign_tokens_until(";", token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
