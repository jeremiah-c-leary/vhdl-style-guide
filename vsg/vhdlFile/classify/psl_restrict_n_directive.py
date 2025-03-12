# -*- coding: utf-8 -*-

from vsg.token.psl import restrict_n_directive as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    [ label : ] Restrict!_Directive

    Assume_Directive ::=
        restrict! Sequence ;
    """

    if utils.are_next_consecutive_tokens([None, ":", "restrict!"], iToken, lObjects) or utils.is_next_token("restrict!", iToken, lObjects):
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("restrict!", token.restrict_n_keyword, iToken, lObjects)
    iCurrent = utils.assign_tokens_until(";", token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
