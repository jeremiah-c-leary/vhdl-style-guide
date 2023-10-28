
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
    lMyUntils = lUntils
    lMyUntils.append(',')

    iCurrent = utils.assign_tokens_until('when', parser.todo, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)

    iCurrent = choices.classify_until(lMyUntils, iCurrent, lObjects)

#    sEnd = utils.find_earliest_occurance_not_in_paren([',', ';'], iCurrent, lObjects)
#    print(f'iCurrent = {iCurrent}||sEnd = {sEnd}')
#    iCurrent = utils.assign_tokens_until_ignoring_paren(sEnd, parser.todo, iCurrent, lObjects)
#    print(f'iCurrent = {iCurrent}||Token Value = {lObjects[iCurrent].get_value()}')

    while utils.is_next_token(',', iCurrent, lObjects):
        print('Got Here')
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_tokens_until('when', parser.todo, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        sEnd = utils.find_earliest_occurance_not_in_paren([',', ';'], iCurrent, lObjects)
        iCurrent = utils.assign_tokens_until_ignoring_paren(sEnd, parser.todo, iCurrent, lObjects)

    print('<-- selected_waveforms.classify')
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
