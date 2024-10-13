# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import external_signal_name as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    """
    external_signal_name ::=
        << signal external_pathname : subtype_indication >>
    """

    if utils.are_next_consecutive_tokens(["<<", "signal"], iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("<<", token.double_less_than, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("signal", token.signal_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.external_pathname, iToken, lObjects)

    while utils.is_next_token("(", iCurrent, lObjects):
        iCurrent = utils.assign_parenthesis_as_todo(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if_not(":", token.external_pathname, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(">>", token.double_greater_than, iToken, lObjects)

    return iCurrent
