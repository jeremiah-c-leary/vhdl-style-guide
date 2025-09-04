# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    element_array_mode_view_indication,
    element_record_mode_view_indication,
)


def detect(iToken, lObjects):
    """
    element_mode_view_indication ::=
        element_record_mode_view_indication
      | element_array_mode_view_indication
    """
    if utils.is_next_token("view", iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    # since element_array_mode_view_indication is more specific, we check it first
    iReturn = element_array_mode_view_indication.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = element_record_mode_view_indication.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
