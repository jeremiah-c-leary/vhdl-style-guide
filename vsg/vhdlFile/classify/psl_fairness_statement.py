# -*- coding: utf-8 -*-

from vsg.token.psl import fairness_statement as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    [ label : ] Fairness_Statement

    Cover_Directive ::=
        fairness Boolean ;
      | strong fairness Boolean, Boolean ;
    """

    if (
        utils.are_next_consecutive_tokens([None, ":", "fairness"], iToken, lObjects)
        or utils.is_next_token("fairness", iToken, lObjects)
        or utils.are_next_consecutive_tokens([None, ":", "strong", "fairness"], iToken, lObjects)
        or utils.are_next_consecutive_tokens(["strong", "fairness"], iToken, lObjects)
    ):
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if("strong", token.strong_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("fairness", token.fairness_keyword, iCurrent, lObjects)

    iCurrent = utils.assign_tokens_until(";", token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
