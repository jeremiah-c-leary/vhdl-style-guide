# -*- coding: utf-8 -*-

from vsg.token import concurrent_signal_assignment_statement as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    concurrent_conditional_signal_assignment,
    concurrent_selected_signal_assignment,
    concurrent_simple_signal_assignment,
)


def detect(oDataStructure):
    """
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    """

    if concurrent_selected_signal_assignment.detect(oDataStructure):
        iCurrent = utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        iCurrent = concurrent_selected_signal_assignment.classify(oDataStructure)
        return True

    elif concurrent_conditional_signal_assignment.detect(oDataStructure):
        iCurrent = utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        iCurrent = concurrent_conditional_signal_assignment.classify(oDataStructure)
        return True

    elif concurrent_simple_signal_assignment.detect(oDataStructure):
        iCurrent = utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(oDataStructure, token.postponed_keyword)
        iCurrent = concurrent_simple_signal_assignment.classify(oDataStructure)
        return True

    return False
