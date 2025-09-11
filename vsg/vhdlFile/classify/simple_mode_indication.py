# -*- coding: utf-8 -*-

from vsg.token import simple_mode_indication as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, mode, subtype_indication


def detect(iToken, lObjects):
    """
    simple_mode_indication ::=
        [ mode ] subtype_indication [ bus ] [ := static_conditional_expression ]
    """

    iCurrent = mode.classify(iToken, lObjects)
    iCurrent = subtype_indication.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if("bus", token.bus_keyword, iCurrent, lObjects)

    if utils.is_next_token(":=", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(":=", token.assignment, iCurrent, lObjects)
        iCurrent = expression.classify_until([";"], iCurrent, lObjects)

    return iCurrent
