# -*- coding: utf-8 -*-

from vsg.token import mode_view_element_definition as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import element_mode_indication, record_element_list


def classify(iToken, lObjects):
    """
    mode_view_element_definition ::=
      record_element_list : element_mode_indication ;
    """
    iCurrent = record_element_list.classify_until([":"], iToken, lObjects)
    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)
    iCurrent = element_mode_indication.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)
    return iCurrent
