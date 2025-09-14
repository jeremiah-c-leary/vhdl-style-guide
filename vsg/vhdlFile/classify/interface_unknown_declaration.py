# -*- coding: utf-8 -*-

from vsg.token import interface_unknown_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier_list, mode_indication


def detect(iToken, lObjects):
    """
    This is a classification if the signal, constant, or variable keywords are not specified.
    This is not in the VHDL LRM.
    It is based off the interface_signal_declaration as it has the most keywords.

    interface_unknown_declaration ::=
        identifier_list : mode_indication
    """

    if utils.is_next_token_one_of(["type", "file", "function", "procedure", "impure", "pure", "package"], iToken, lObjects):
        return iToken
    else:
        return classify(iToken, lObjects)


def classify(iToken, lObjects):
    iCurrent = identifier_list.classify_until([":"], iToken, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)

    iCurrent = mode_indication.classify(iCurrent, lObjects)

    return iCurrent
