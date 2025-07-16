# -*- coding: utf-8 -*-

from vsg.token import array_mode_view_indication as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    """
    array_mode_view_indication ::=
        view ( mode_view_name ) of unresolved_array_subtype_indication
    """
    if utils.are_next_consecutive_tokens(["view", "("], iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("view", token.view_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)

    iCurrent = utils.assign_next_token(token.name, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    if utils.is_next_token("of", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("of", token.of_keyword, iCurrent, lObjects)

        iCurrent = subtype_indication.classify(iCurrent, lObjects)

    return iCurrent
