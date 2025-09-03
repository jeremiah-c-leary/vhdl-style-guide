# -*- coding: utf-8 -*-


from vsg.vhdlFile.classify import mode_view_indication, simple_mode_indication


def classify(iToken, lObjects):
    """
    mode_indication ::=
        simple_mode_indication
        | mode_view_indication

    """

    # We need to check mode_view_indication first since it always starts with "view"
    iReturn = mode_view_indication.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return simple_mode_indication.detect(iToken, lObjects)
