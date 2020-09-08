
from vsg import parser

from vsg.token import concurrent_simple_signal_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import delay_mechanism


def detect(iCurrent, lObjects):
    '''

    [ label : ] [ postponed ] concurrent_simple_signal_assignment

    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;

    The key to detecting this is looking for an assignment <= followed by a semicolon.
    This will be the default if the other types are not found.
    '''

    iToken = iCurrent

    while lObjects[iToken].get_value() != ';':
        if utils.is_item(lObjects, iToken):
            if utils.object_value_is(lObjects, iToken, 'when'):
                return False
            if lObjects[iToken].get_value() == '<=':
                return True
        iToken += 1
    else:
        return False


def classify(iToken, lObjects):
    '''
    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;
    '''
    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('guarded', token.guarded_keyword, iCurrent, lObjects)
    iCurrent = delay_mechanism.detect(iCurrent, lObjects)
    iCurrent = utils.assign_tokens_until(';', parser.todo, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
