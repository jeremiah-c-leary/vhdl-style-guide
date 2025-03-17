# -*- coding: utf-8 -*-

from vsg.token import interface_incomplete_type_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_incomplete_type_declaration ::=
        type identifier
    """
    return oDataStructure.is_next_token("type")


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if("type", token.type_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)

    return iCurrent
