# -*- coding: utf-8 -*-

from vsg.token import concurrent_signal_assignment_statement as token
from vsg.vhdlFile.classify import (
    concurrent_conditional_signal_assignment,
    concurrent_selected_signal_assignment,
    concurrent_simple_signal_assignment,
    utils,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    """

    if concurrent_selected_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        concurrent_selected_signal_assignment.classify(oDataStructure)
        return True

    elif concurrent_conditional_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        concurrent_conditional_signal_assignment.classify(oDataStructure)
        return True

    elif concurrent_simple_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        concurrent_simple_signal_assignment.classify(oDataStructure)
        return True

    return False
