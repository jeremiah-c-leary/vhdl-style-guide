
from vsg import parser

from vsg.token import choices as token

from vsg.vhdlFile import utils


def classify(iStart, iEnd, lObjects):
    '''
    choices ::=
        choice { | choice }
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
            utils.assign_token(lObjects, iToken, parser.todo)

    return iEnd


def classify_until(lUntils, iToken, lObjects):
    iCurrent = iToken
    iLast = 0
    lMyUntils = lUntils.append('|')

    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = choice.classify_until(lMyUntils, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if('|', token.bar, iCurrent, lObjects)

    return iCurrent
