# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import conditional_variable_assignment as token
from vsg.vhdlFile.classify import conditional_expressions, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    conditional_variable_assignment ::=
        target := conditional_expressions ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string(":=", ";"):
        if not oDataStructure.does_string_exist_before_string("with", ";"):
            if oDataStructure.does_string_exist_before_string("when", ";"):
                return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.assign_tokens_until(":=", token.target, oDataStructure)

    oDataStructure.replace_next_token_required(":=", token.assignment)

    conditional_expressions.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
