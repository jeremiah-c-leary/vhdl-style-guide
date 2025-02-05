# -*- coding: utf-8 -*-

from vsg.token import subtype_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier, subtype_indication


def detect(oDataStructure):
    """
    subtype_declaration ::=
        subtype identifier is subtype_indication ;
    """

    if oDataStructure.is_next_token("subtype"):
        classify(oDataStructure)
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("subtype", token.subtype_keyword, iToken, lObjects)

    iCurrent = identifier.classify(iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
