# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_force_assignment as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, force_mode


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_force_assignment ::=
        target <= force [ force_mode ] expression ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        return oDataStructure.does_string_exist_before_string("force", ";")
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_tokens_until("<=", token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("<=", token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("force", token.force_keyword, iCurrent, lObjects)

    iCurrent = force_mode.detect(iCurrent, lObjects)
    iCurrent = expression.classify_until([";"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
