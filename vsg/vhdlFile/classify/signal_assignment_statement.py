# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import signal_assignment_statement as token
from vsg.vhdlFile.classify import (
    conditional_signal_assignment,
    selected_signal_assignment,
    simple_signal_assignment,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    signal_assignment_statement ::=
        [ label : ] simple_signal_assignment
      | [ label : ] conditional_signal_assignment
      | [ label : ] selected_signal_assignment
    """

    if selected_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label, token.label_colon)
        selected_signal_assignment.classify(oDataStructure)
        return True

    if conditional_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label, token.label_colon)
        conditional_signal_assignment.classify(oDataStructure)
        return True

    if simple_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label, token.label_colon)
        simple_signal_assignment.classify(oDataStructure)
        return True

    return False
