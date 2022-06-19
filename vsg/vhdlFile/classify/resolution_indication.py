
from vsg import parser

from vsg.token import resolution_indication as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    resolution_indication ::=
        resolution_function_name | ( element_resolution )
    '''
    if utils.is_next_token('(', iToken, lObjects):
        return classify(iToken, lObjects)
    else:
        iTemp = utils.find_next_token(iToken, lObjects) + 1
        if utils.is_next_token('(', iTemp, lObjects):
            return iToken
        if utils.is_next_token(')', iTemp, lObjects):
            return iToken
        if utils.is_next_token(';', iTemp, lObjects):
            return iToken
        if utils.is_next_token(':=', iTemp, lObjects):
            return iToken
        if utils.is_next_token('range', iTemp, lObjects):
            return iToken
        if utils.is_next_token('bus', iTemp, lObjects):
            return iToken
        if utils.is_next_token('is', iTemp, lObjects):
            return iToken
        if utils.is_next_token('open', iTemp, lObjects):
            return iToken
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = iToken

    if utils.is_next_token('(', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
        iCurrent = utils.assign_tokens_until_matching_closing_paren(parser.todo, iCurrent, lObjects)
    else:
        iCurrent = utils.assign_next_token(token.resolution_function_name, iCurrent, lObjects)

    return iCurrent
