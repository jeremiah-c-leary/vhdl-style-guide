# -*- coding: utf-8 -*-

from vsg.token import variable_assignment_statement as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    conditional_variable_assignment,
    selected_variable_assignment,
    simple_variable_assignment,
)


def detect(iToken, lObjects):
    """
    variable_assignment_statement ::=
        [ label : ] simple_variable_assignment
      | [ label : ] conditional_variable_assignment
      | [ label : ] selected_variable_assignment
    """
    iCurrent = iToken
    if selected_variable_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label, token.label_colon)
        iCurrent = selected_variable_assignment.classify(iCurrent, lObjects)

    elif conditional_variable_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label, token.label_colon)
        iCurrent = conditional_variable_assignment.classify(iCurrent, lObjects)

    elif simple_variable_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label, token.label_colon)
        iCurrent = simple_variable_assignment.classify(iCurrent, lObjects)

    return iCurrent
