# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import iteration_scheme as token
from vsg.vhdlFile.classify import condition, parameter_specification


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    iteration_scheme ::=
        while condition
      | for *loop*_parameter_specification
    """
    if oDataStructure.does_string_exist_in_next_n_tokens(";", 3):
        return False
    if oDataStructure.does_string_exist_in_next_n_tokens("else", 3):
        return False
    if oDataStructure.does_string_exist_in_next_n_tokens("while", 3):
        return True
    if oDataStructure.does_string_exist_in_next_n_tokens("for", 3):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if oDataStructure.is_next_token("while"):
        oDataStructure.replace_next_token_required("while", token.while_keyword)
        condition.classify_until(["loop"], oDataStructure)

    if oDataStructure.is_next_token("for"):
        oDataStructure.replace_next_token_required("for", token.for_keyword)
        parameter_specification.classify_until(["loop"], oDataStructure)
