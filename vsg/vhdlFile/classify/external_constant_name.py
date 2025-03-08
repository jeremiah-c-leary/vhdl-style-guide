# -*- coding: utf-8 -*-

from vsg.token import external_constant_name as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subtype_indication
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    external_constant_name ::=
        << constant external_pathname : subtype_indication >>
    """

    if oDataStructure.are_next_consecutive_tokens(["<<", "constant"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("<<", token.double_less_than, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("constant", token.constant_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.external_pathname, iCurrent, lObjects)

    while utils.is_next_token("(", iCurrent, lObjects):
        iCurrent = utils.assign_parenthesis_as_todo(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if_not(":", token.external_pathname, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(">>", token.double_greater_than, iCurrent, lObjects)

    return iCurrent
