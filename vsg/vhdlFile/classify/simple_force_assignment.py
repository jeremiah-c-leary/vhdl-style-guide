# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_force_assignment as token
from vsg.vhdlFile.classify import expression, force_mode, utils


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
def classify(oDataStructure):
    utils.assign_tokens_until("<=", token.target, oDataStructure)
    oDataStructure.replace_next_token_required("<=", token.assignment)
    oDataStructure.replace_next_token_required("force", token.force_keyword)

    force_mode.detect(oDataStructure)
    expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
