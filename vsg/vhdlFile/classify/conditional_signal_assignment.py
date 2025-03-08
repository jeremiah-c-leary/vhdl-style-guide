# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    conditional_force_assignment,
    conditional_waveform_assignment,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    conditional_signal_assignment ::=
        conditional_waveform_assignment
      | conditional_force_assignment
    """

    if oDataStructure.is_next_token("when"):
        return False
    if oDataStructure.does_string_exist_in_next_n_tokens("if", 3):
        return False
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if oDataStructure.does_string_exist_before_string("when", ";"):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = conditional_force_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = conditional_waveform_assignment.detect(iToken, lObjects)

    return iCurrent
