
from vsg.token import enumeration_type_definition as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    enumeration_type_definition ::=
        ( enumeration_literal { , enumeration_literal } )
    '''
    if utils.is_next_token('(', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iToken, lObjects)

    while not utils.is_next_token(')', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.enumeration_literal, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    return iCurrent
