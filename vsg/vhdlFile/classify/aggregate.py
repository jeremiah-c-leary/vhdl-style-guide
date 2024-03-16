# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils


def classify(iToken, lObjects, oTokenClass):
    """
    aggregate ::=
        ( element_association { , element_association } )
    """
    iCurrent = utils.assign_next_token_required("(", oTokenClass.aggregate_open_parenthesis, iToken, lObjects)
    iCurrent = utils.assign_next_token(oTokenClass.simple_name, iCurrent, lObjects)

    while utils.is_next_token(",", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(",", oTokenClass.aggregate_comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(oTokenClass.simple_name, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(")", oTokenClass.aggregate_close_parenthesis, iToken, lObjects)

    return iCurrent
