
from vsg.token import choices as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import choice


def classify_until(lUntils, iToken, lObjects):
    '''
    choices ::=
        choice { | choice }
    '''
    iCurrent = iToken
    iLast = 0
    lMyUntils = lUntils
    lMyUntils.append('|')

    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = choice.classify_until(lMyUntils, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if('|', token.bar, iCurrent, lObjects)

    return iCurrent
