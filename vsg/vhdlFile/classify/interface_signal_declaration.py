# -*- coding: utf-8 -*-


from vsg.token import interface_signal_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier_list, mode_indication


def detect(iToken, lObjects):
    """
    interface_signal_declaration ::=
          signal identifier_list : mode_indication
    """

    if utils.is_next_token("signal", iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("signal", token.signal_keyword, iToken, lObjects)

    iCurrent = identifier_list.classify_until([":"], iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)

    iCurrent = mode_indication.classify(iCurrent, lObjects)

    return iCurrent
