# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_waveform_assignment as token
from vsg.vhdlFile.classify import delay_mechanism, utils, waveform


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_waveform_assignment ::=
        target <= [ delay_mechanism ] waveform ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    return is_a_simple_waveform_assignment(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.assign_tokens_until("<=", token.target, oDataStructure)
    oDataStructure.replace_next_token_required("<=", token.assignment)

    delay_mechanism.detect(oDataStructure)

    waveform.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)


@decorators.print_classifier_debug_info(__name__)
def is_a_simple_waveform_assignment(oDataStructure):
    if utils.assignment_operator_found(oDataStructure):
        if force_or_release_keyword_found(oDataStructure):
            return False
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def force_or_release_keyword_found(oDataStructure):
    if oDataStructure.does_string_exist_before_string("force", ";"):
        return True
    return oDataStructure.does_string_exist_before_string("release", ";")
