# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import element_mode_view_indication, mode


def classify(iToken, lObjects):
    """
    element_mode_indication ::=
      mode
      | element_mode_view_indication
    """
    iReturn = mode.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = element_mode_view_indication.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
