# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile import utils
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

    if oDataStructure.does_string_exist_in_next_n_tokens("if", 3):
        return False
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if oDataStructure.does_string_exist_before_string("with", ";"):
            return False
        if oDataStructure.does_string_exist_before_string("when", ";"):
            return False
        return True
    return False


#    if utils.find_in_next_n_tokens("if", 3, iToken, lObjects):
#        return False
#    if utils.find_in_range("<=", iToken, ";", lObjects):
#        if utils.find_in_range("when", iToken, ";", lObjects):
#            return False
#        if utils.find_in_range("with", iToken, ";", lObjects):
#            return False
#        return True
#    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = iToken
    iCurrent = simple_force_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = simple_release_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = simple_waveform_assignment.detect(iToken, lObjects)

    return iCurrent
