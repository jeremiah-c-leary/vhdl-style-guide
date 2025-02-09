# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    selected_force_assignment,
    selected_waveform_assignment,
)


def detect(oDataStructure):
    """
    selected_signal_assignment ::=
        selected_waveform_assignment
      | selected_force_assignment
    """

    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if oDataStructure.doess_string_exist_in_next_n_tokens("with", 3):
            return True
        if oDataStructure.doess_string_exist_in_next_n_tokens("if", 3):
            return True
    return False


def classify(iToken, lObjects):
    iCurrent = selected_waveform_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = selected_force_assignment.detect(iToken, lObjects)

    return iCurrent
