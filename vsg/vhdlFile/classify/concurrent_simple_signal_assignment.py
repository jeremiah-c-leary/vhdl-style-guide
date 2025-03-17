# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_simple_signal_assignment as token
from vsg.vhdlFile.classify import delay_mechanism, utils, waveform


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    [ label : ] [ postponed ] concurrent_simple_signal_assignment

    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;

    The key to detecting this is looking for an assignment <= followed by a semicolon.
    This will be the default if the other types are not found.
    """

    if oDataStructure.does_string_exist_before_string_honoring_parenthesis_hierarchy("<=", ";"):
        if oDataStructure.does_string_exist_before_string("when", ";"):
            return False
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.assign_tokens_until("<=", token.target, oDataStructure)
    oDataStructure.replace_next_token_required("<=", token.assignment)
    oDataStructure.replace_next_token_with_if("guarded", token.guarded_keyword)

    delay_mechanism.detect(oDataStructure)

    waveform.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
