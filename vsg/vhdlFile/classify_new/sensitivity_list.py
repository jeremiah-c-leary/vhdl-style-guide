
from vsg import parser

from vsg.token import sensitivity_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    '''

    iCurrent = iToken
    iLast = 0
    while iLast != iCurrent:
        iLast = iCurrent
        if utils.is_next_token(')', iCurrent, lObjects):
            return iCurrent
        if utils.is_next_token('on', iCurrent, lObjects):
            return iCurrent
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)

def classify_until(lUntils, iToken, lObjects):
    '''
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    '''

    iCurrent = iToken
    iLast = 0
    while iLast != iCurrent:
        iLast = iCurrent
        if lObjects[utils.find_next_token(iCurrent, lObjects)].get_value() in lUntils:
            return iCurrent
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)
