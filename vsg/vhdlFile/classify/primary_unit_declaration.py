# -*- coding: utf-8 -*-

from vsg.token import primary_unit_declaration as token
from vsg.vhdlFile import utils
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    primary_unit_declaration ::= identifier;
    """
    return classify(iToken, lObjects)


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = iToken

    while not utils.is_next_token(";", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_token(lObjects, iCurrent, token.semicolon)

    return iCurrent
