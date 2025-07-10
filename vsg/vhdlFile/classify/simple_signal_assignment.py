# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    simple_force_assignment,
    simple_release_assignment,
    simple_waveform_assignment,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_signal_assignment ::=
        simple_waveform_assignment
      | simple_force_assignment
      | simple_release_assignment
    """

    if oDataStructure.is_next_token_one_of(["if", "elsif", "else"]):
        return False

    if oDataStructure.does_string_exist_before_string_honoring_parenthesis_hierarchy("<=", ";"):
        if oDataStructure.does_string_exist_before_string("with", ";"):
            return False
        if oDataStructure.does_string_exist_before_string("when", ";"):
            return False
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if simple_force_assignment.detect(oDataStructure):
        simple_force_assignment.classify(oDataStructure)
    elif simple_release_assignment.detect(oDataStructure):
        simple_release_assignment.classify(oDataStructure)
    elif simple_waveform_assignment.detect(oDataStructure):
        simple_waveform_assignment.classify(oDataStructure)
