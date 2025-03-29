# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import external_variable_name as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    external_variable_name ::=
        << variable external_pathname : subtype_indication >>
    """

    if oDataStructure.are_next_consecutive_tokens(["<<", "variable"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.double_less_than)
    oDataStructure.replace_next_token_with(token.variable_keyword)
    oDataStructure.replace_next_token_with(token.external_pathname)

    while oDataStructure.is_next_token("("):
        iCurrent = utils.assign_parenthesis_as_todo(iCurrent, lObjects)
        oDataStructure.replace_next_token_with_if_not(":", token.external_pathname)

    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)

    oDataStructure.replace_next_token_required(">>", token.double_greater_than)
