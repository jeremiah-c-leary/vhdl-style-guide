# -*- coding: utf-8 -*-

from vsg.token import element_record_mode_view_indication as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    element_record_mode_view_indication ::=
        view mode_view_name

    """
    if utils.is_next_token("view", iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("view", token.view_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.name, iCurrent, lObjects)

    return iCurrent
