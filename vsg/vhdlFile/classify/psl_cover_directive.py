# -*- coding: utf-8 -*-

from vsg.token.psl import cover_directive as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    [ label : ] Cover_Directive

    Cover_Directive ::=
        cover Sequence [ report String ] ;
    """

    if utils.are_next_consecutive_tokens([None, ":", "cover"], iToken, lObjects) or utils.is_next_token("cover", iToken, lObjects):
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("cover", token.cover_keyword, iToken, lObjects)
    iCurrent = utils.assign_tokens_until(";", token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
