
from vsg.token import identifier as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    identifier ::=
        basic_identifier | extended_identifier
    '''

    return utils.assign_next_token(token.identifier, iToken, lObjects)
