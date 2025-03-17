# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_conditional_signal_assignment as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import conditional_waveforms, delay_mechanism


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
    oDataStructure.align_seek_index()
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
def classify(iToken, lObjects):
    """
    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;
    """
    iCurrent = utils.assign_tokens_until("<=", token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("<=", token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if("guarded", token.guarded_keyword, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    iCurrent = conditional_waveforms.classify_until([";"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
