
from vsg import parser

from vsg.token import selected_waveforms as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import choices
from vsg.vhdlFile.classify import waveform


def classify(iToken, lObjects):
    '''
    selected_waveforms ::=
        { waveform when choices , }
        waveform when choices
    '''
    iCurrent = iToken

    iCurrent = utils.assign_tokens_until('when', parser.todo, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
    sEnd = utils.find_earliest_occurance([',', ';'], iCurrent, lObjects)
    iCurrent = utils.assign_tokens_until(sEnd, parser.todo, iCurrent, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_tokens_until('when', parser.todo, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        sEnd = utils.find_earliest_occurance([',', ';'], iCurrent, lObjects)
        iCurrent = utils.assign_tokens_until(sEnd, parser.todo, iCurrent, lObjects)

    return iCurrent


def classify_until(lUntils, iToken, lObjects):
    '''
    selected_waveforms ::=
        { waveform when choices , }
        waveform when choices
    '''
    iCurrent = iToken
    lMyUntils = lUntils
    lMyUntils.append(',')

    iCurrent = waveform.classify_until(['when'], iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
    iCurrent = choices.classify_until(lMyUntils, iCurrent, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = waveform.classify_until(['when'], iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        iCurrent = choices.classify_until(lMyUntils, iCurrent, lObjects)

    return iCurrent
