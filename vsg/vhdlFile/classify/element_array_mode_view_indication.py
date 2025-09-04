# -*- coding: utf-8 -*-

from vsg.token import element_array_mode_view_indication as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    element_array_mode_view_indication ::=
        view ( mode_view_name )
    """
    if utils.are_next_consecutive_tokens(["view", "(", None, ")"], iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("view", token.view_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)

    iCurrent = utils.assign_next_token(token.name, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
