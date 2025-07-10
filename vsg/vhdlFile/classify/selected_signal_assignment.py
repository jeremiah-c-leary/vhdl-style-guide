# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    selected_force_assignment,
    selected_waveform_assignment,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    selected_signal_assignment ::=
        selected_waveform_assignment
      | selected_force_assignment
    """

    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if oDataStructure.does_string_exist_in_next_n_tokens("with", 3):
            return True
        if oDataStructure.does_string_exist_in_next_n_tokens("if", 3):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if selected_waveform_assignment.detect(oDataStructure):
        return None

    selected_force_assignment.detect(oDataStructure)
