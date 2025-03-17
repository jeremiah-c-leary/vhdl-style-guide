# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_variable_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, identifier_list, mode, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_variable_declaration ::=
    [ variable ] identifier_list : [ mode ] subtype_indication [ := static_expression ]
    """

    return oDataStructure.is_next_token("variable")


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("variable", token.variable_keyword, iToken, lObjects)

    iCurrent = identifier_list.classify_until([":"], iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)

    iCurrent = mode.classify(iCurrent, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    if utils.is_next_token(":=", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(":=", token.assignment, iCurrent, lObjects)
        iCurrent = expression.classify_until([";"], iCurrent, lObjects)

    return iCurrent
