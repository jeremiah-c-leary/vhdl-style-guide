
from vsg.token import concurrent_simple_signal_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import delay_mechanism
from vsg.vhdlFile.classify import waveform


def detect(iToken, lObjects):
    '''
    [ label : ] [ postponed ] concurrent_simple_signal_assignment

    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;

    The key to detecting this is looking for an assignment <= followed by a semicolon.
    This will be the default if the other types are not found.
    '''

    iCurrent = iToken

    while lObjects[iCurrent].get_value() != ';':
        if utils.is_item(lObjects, iCurrent):
            if utils.object_value_is(lObjects, iCurrent, 'when'):
                return False
            if lObjects[iCurrent].get_value() == '<=':
                return True
        iCurrent += 1

    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('guarded', token.guarded_keyword, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    iCurrent = waveform.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
