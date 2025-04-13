# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import variable_assignment_statement as token
from vsg.vhdlFile.classify import (
    conditional_variable_assignment,
    selected_variable_assignment,
    simple_variable_assignment,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    variable_assignment_statement ::=
        [ label : ] simple_variable_assignment
      | [ label : ] conditional_variable_assignment
      | [ label : ] selected_variable_assignment
    """
    if selected_variable_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label, token.label_colon)
        selected_variable_assignment.classify(oDataStructure)
        return True

    if conditional_variable_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label, token.label_colon)
        conditional_variable_assignment.classify(oDataStructure)
        return True

    if simple_variable_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label, token.label_colon)
        simple_variable_assignment.classify(oDataStructure)
        return True

    return False
