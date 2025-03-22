# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_release_assignment as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import force_mode


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_release_assignment ::=
        target <= release [ force_mode ] ;
    """

    return oDataStructure.does_string_exist_before_string("release", ";")


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_tokens_until("<=", token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("<=", token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("release", token.release_keyword, iCurrent, lObjects)

    iCurrent = force_mode.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
