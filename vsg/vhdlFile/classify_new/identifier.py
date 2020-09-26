
from vsg.token import identifier as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects, oType=token.identifier):
    '''
    identifier ::=
        basic_identifier | extended_identifier
    '''

    return utils.assign_next_token(oType, iToken, lObjects)
