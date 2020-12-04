
from vsg.token import concurrent_conditional_signal_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import delay_mechanism
from vsg.vhdlFile.classify import conditional_waveforms


def detect(iToken, lObjects):
    '''

    [ label : ] [ postponed ] concurrent_conditional_signal_assignment

    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;

    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]

    The key to detecting this is looking for an assignment <= followed by the keyword **when** before a semicolon.
    '''

    iCurrent = iToken
    bAssignmentFound = False

    while lObjects[iCurrent].get_value() != ';':
        if utils.is_item(lObjects, iCurrent):
            if bAssignmentFound:
                if utils.object_value_is(lObjects, iCurrent, 'when'):
                    return True
            else:
                if utils.object_value_is(lObjects, iCurrent, 'when'):
                    return False
                if utils.object_value_is(lObjects, iCurrent, 'with'):
                    return False

            if utils.object_value_is(lObjects, iCurrent, '<=') and not bAssignmentFound:
                bAssignmentFound = True
        iCurrent += 1

    return False


def classify(iToken, lObjects):
    '''
    concurrent_conditional_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] conditional_waveforms ;
    '''
    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('guarded', token.guarded_keyword, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    iCurrent = conditional_waveforms.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
