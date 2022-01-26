
from vsg.token import secondary_unit_declaration as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    secondary_unit_declaration ::= identifier = physical_literal;
    '''
    if utils.find_in_range('=', iToken, ';', lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = iToken
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.equal_sign, iCurrent, lObjects)

    while not utils.is_next_token(';', iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.physical_literal, iCurrent, lObjects)
    iCurrent = utils.assign_token(lObjects, iCurrent, token.semicolon)

    return iCurrent
