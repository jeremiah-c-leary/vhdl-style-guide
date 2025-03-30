# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_conditional_signal_assignment as token
from vsg.vhdlFile.classify import conditional_waveforms, delay_mechanism, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """

    [ label : ] [ postponed ] concurrent_conditional_signal_assignment

    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;

    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]

    The key to detecting this is looking for an assignment <= followed by the keyword **when** before a semicolon.
    """

    bAssignmentFound = False
    while not oDataStructure.seek_token_lower_value_is(";"):
        if bAssignmentFound:
            if oDataStructure.seek_token_lower_value_is("when"):
                return True
        else:
            if oDataStructure.seek_token_lower_value_is("when"):
                return False
            if oDataStructure.seek_token_lower_value_is("with"):
                return False

            if oDataStructure.seek_token_lower_value_is("<="):
                bAssignmentFound = True

        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()

    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;
    """
    utils.assign_tokens_until("<=", token.target, oDataStructure)

    oDataStructure.replace_next_token_required("<=", token.assignment)

    oDataStructure.replace_next_token_with_if("guarded", token.guarded_keyword)

    delay_mechanism.detect(oDataStructure)

    conditional_waveforms.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
