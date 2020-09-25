
from vsg.token import identifier_list as token

from vsg.vhdlFile import utils


def classify_until(lUntils, iToken, lObjects, oToken=token.identifier):
    '''
    identifier_list ::=
        identifier { , identifier }
    '''
    iEnd = len(lObjects) - 1
    iCurrent = iToken

    while not utils.is_next_token_one_of(lUntils, iCurrent, lObjects):
        if iCurrent == iEnd:
            return iCurrent
        iCurrent = utils.assign_next_token_if_not(',', oToken, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)

    return iCurrent
