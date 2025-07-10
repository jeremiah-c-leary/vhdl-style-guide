# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_variable_assignment as token
from vsg.vhdlFile.classify import expression, target


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_variable_assignment ::=
        target := expression ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string(":=", ";"):
        if oDataStructure.does_string_exist_before_string("with", ";"):
            return False
        if oDataStructure.does_string_exist_before_string("when", ";"):
            return False
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    target.classify(oDataStructure, token)
    oDataStructure.replace_next_token_required(":=", token.assignment)

    expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
