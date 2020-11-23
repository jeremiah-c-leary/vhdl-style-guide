
from vsg.token import simple_waveform_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import delay_mechanism
from vsg.vhdlFile.classify import waveform


def detect(iToken, lObjects):
    '''
    simple_waveform_assignment ::=
        target <= [ delay_mechanism ] waveform ;
    '''

    if utils.is_next_token_one_of(['when', 'if', 'elsif', 'else'], iToken, lObjects):
        return False
    if utils.find_in_range('<=', iToken, ';', lObjects):
        if utils.find_in_range('force', iToken, ';', lObjects):
            return iToken
        if utils.find_in_range('release', iToken, ';', lObjects):
            return iToken
    return classify(iToken, lObjects)


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    iCurrent = waveform.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
