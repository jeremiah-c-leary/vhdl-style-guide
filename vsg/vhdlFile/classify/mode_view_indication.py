# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    array_mode_view_indication,
    record_mode_view_indication,
)


def detect(iToken, lObjects):
    """
    mode_view_indication ::=
        record_mode_view_indication
      | array_mode_view_indication
    """

    # We need to check array_mode_view_indication first since it has a more specific syntax
    iReturn = array_mode_view_indication.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = record_mode_view_indication.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
