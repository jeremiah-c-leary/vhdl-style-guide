
from vsg.token import conditional_waveforms as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import waveform
from vsg.vhdlFile.classify import condition


def classify_until(lUntils, iToken, lObjects):
    '''
    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]
    '''

    lMyElseUntils = lUntils.copy()
    lMyElseUntils.append('else')
    lMyWhenUntils = lUntils.copy()
    lMyWhenUntils.append('when')

    iCurrent = waveform.classify_until(['when'], iToken, lObjects)
    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
    iCurrent = condition.classify_until(lMyElseUntils, iCurrent, lObjects)

    while utils.is_next_token('else', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('else', token.else_keyword, iCurrent, lObjects)
        iCurrent = waveform.classify_until(lMyWhenUntils, iCurrent, lObjects)
        if utils.is_next_token_in_list(lUntils, iToken, lObjects):
            break
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until(lMyElseUntils, iCurrent, lObjects)

    return iCurrent
