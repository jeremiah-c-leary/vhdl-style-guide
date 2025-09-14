# -*- coding: utf-8 -*-

from vsg.token import record_element_list as token
from vsg.vhdlFile import utils


def classify_until(lUntils, iToken, lObjects, oToken=token.simple_name):
    """
    record_element_list ::=
      record_element_simple_name { , record_element_simple_name }

    """
    iEnd = len(lObjects) - 1
    iCurrent = iToken

    while not utils.is_next_token_one_of(lUntils, iCurrent, lObjects):
        if iCurrent == iEnd:
            return iCurrent
        iCurrent = utils.assign_next_token_if_not(",", oToken, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if(",", token.comma, iCurrent, lObjects)

    return iCurrent
