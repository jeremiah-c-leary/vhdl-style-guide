
from vsg.token import logical_name_list as token

from vsg.vhdlFile import utils


def classify_until(lUntils, iToken, lObjects):
    '''
    logical_name_list ::=
        logical_name { , logical_name }
    '''
    iCurrent = iToken
    iLast = 0
    while iLast != iCurrent:
        iLast = iCurrent
        if lObjects[utils.find_next_token(iCurrent, lObjects)].get_value().lower() in lUntils:
            return iCurrent
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.logical_name, iCurrent, lObjects)
