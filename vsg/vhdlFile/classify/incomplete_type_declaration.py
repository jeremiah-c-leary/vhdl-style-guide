# -*- coding: utf-8 -*-

from vsg.token import incomplete_type_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    incomplete_type_declaration ::=
        type identifier ;
    """
    if oDataStructure.are_next_consecutive_tokens(["type", None, ";"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("type", token.type_keyword, iToken, lObjects)

    iCurrent = identifier.classify(iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
