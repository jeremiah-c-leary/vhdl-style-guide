# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_signal_assignment_statement as token
from vsg.vhdlFile.classify import (
    concurrent_conditional_signal_assignment,
    concurrent_selected_signal_assignment,
    concurrent_simple_signal_assignment,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    """

    oDataStructure.align_seek_index()
    if concurrent_selected_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        concurrent_selected_signal_assignment.classify(oDataStructure)
        return True

    oDataStructure.align_seek_index()
    if concurrent_conditional_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        concurrent_conditional_signal_assignment.classify(oDataStructure)
        return True

    oDataStructure.align_seek_index()
    if concurrent_simple_signal_assignment.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        concurrent_simple_signal_assignment.classify(oDataStructure)
        return True

    return False
