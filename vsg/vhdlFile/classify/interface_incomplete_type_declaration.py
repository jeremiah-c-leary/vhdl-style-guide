# -*- coding: utf-8 -*-

from vsg.token import interface_incomplete_type_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier


def detect(iToken, lObjects):
    """
    interface_incomplete_type_declaration ::=
        type identifier [ is (<>) ]
    """
    if utils.is_next_token("type", iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if("type", token.type_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects, token.identifier)

    if utils.is_next_token("is", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required("<>", token.undefined_range, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
