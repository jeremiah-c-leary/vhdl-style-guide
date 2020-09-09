
from vsg.token import identifier_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    identifier_list ::=
        identifier { , identifier }
    '''
    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        # the sensitivity list ends in a colon, so we can use it to break out of this while loop
        if utils.is_next_token(':', iCurrent, lObjects):
            break
        if utils.is_next_token('is', iCurrent, lObjects):
            break
        elif utils.is_next_token(',', iCurrent, lObjects):
            utils.classify_next_token(token.comma, iCurrent, lObjects)
        else:
            utils.classify_next_token(token.identifier, iCurrent, lObjects)
        iCurrent += 1
    return iCurrent
