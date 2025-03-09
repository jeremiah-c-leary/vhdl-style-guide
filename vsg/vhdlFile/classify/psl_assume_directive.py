# -*- coding: utf-8 -*-

from vsg.token.psl import assume_directive as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    [ label : ] Assume_Directive

    Assume_Directive ::=
        assume Property ;
    """

    if utils.are_next_consecutive_tokens([None, ":", "assume"], iToken, lObjects) or utils.is_next_token("assume", iToken, lObjects):
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("assume", token.assume_keyword, iToken, lObjects)
    iCurrent = utils.assign_tokens_until(";", token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
