
from vsg.token import identifier_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    identifier_list ::=
        identifier { , identifier }
    '''
    iCurrent = utils.assign_next_token(token.identifier, iToken, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iToken, lObjects)
        iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)

    return iCurrent
