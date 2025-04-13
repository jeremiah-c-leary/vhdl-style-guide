# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import conditional_force_assignment as token
from vsg.vhdlFile.classify import conditional_expressions, force_mode, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    conditional_force_assignment ::=
        target <= force [ force_mode ] conditional_expressions ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if oDataStructure.does_string_exist_before_string("force", ";"):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.assign_tokens_until("<=", token.target, oDataStructure)

    oDataStructure.replace_next_token_required("<=", token.assignment)

    oDataStructure.replace_next_token_required("force", token.force_keyword)

    force_mode.detect(oDataStructure)

    conditional_expressions.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
