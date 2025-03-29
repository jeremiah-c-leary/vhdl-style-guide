# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import conditional_waveform_assignment as token
from vsg.vhdlFile.classify import conditional_waveforms, delay_mechanism, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    conditional_waveform_assignment ::=
        target <= [ delay_mechanism ] conditional_waveforms ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if not oDataStructure.does_string_exist_before_string("force", ";"):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.assign_tokens_until("<=", token.target, oDataStructure)
    oDataStructure.replace_next_token_required("<=", token.assignment)

    delay_mechanism.detect(oDataStructure)

    conditional_waveforms.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
