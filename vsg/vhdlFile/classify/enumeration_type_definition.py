# -*- coding: utf-8 -*-

from vsg.token import enumeration_type_definition as token
from vsg.vhdlFile import utils
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    enumeration_type_definition ::=
        ( enumeration_literal { , enumeration_literal } )
    """
    if oDataStructure.is_next_token("("):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iToken, lObjects)

    while not utils.is_next_token(")", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_if(",", token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.enumeration_literal, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)
    return iCurrent
