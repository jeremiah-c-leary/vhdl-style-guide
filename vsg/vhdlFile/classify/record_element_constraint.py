# -*- coding: utf-8 -*-

from vsg.token import record_element_constraint as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import element_constraint


def detect(oDataStructure):
    """
    record_element_constraint ::=
        record_element_simple_name element_constraint
    """
    if not oDataStructure.is_next_seek_token("("):
        oDataStructure.increment_seek_index()
        if oDataStructure.is_next_seek_token("("):
            return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token(token.record_element_simple_name, iToken, lObjects)
    iCurrent = element_constraint.detect(iCurrent, lObjects)

    return iCurrent
