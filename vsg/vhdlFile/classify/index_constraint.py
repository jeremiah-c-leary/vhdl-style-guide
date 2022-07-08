
from vsg.token import index_constraint as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import discrete_range


def detect(iToken, lObjects):
    '''
    index_constraint ::=
        ( discrete_range { , discrete_range } )
    '''
    if utils.is_next_token('(', iToken, lObjects):
        iCurrent = utils.find_next_token(iToken, lObjects) + 1
        if discrete_range.detect(iCurrent, lObjects):
            return True
    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iToken, lObjects)

    while not utils.is_next_token(')', iCurrent, lObjects):
        iCurrent = discrete_range.classify_until([','], iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    return iCurrent
