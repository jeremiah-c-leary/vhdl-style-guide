
from vsg import parser

from vsg.token import resolution_indication as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    resolution_indication ::=
        resolution_function_name | ( element_resolution )
    '''
    if detect_element_resolution(iToken, lObjects):
        return classify_element_resolution(iToken, lObjects)
    elif detect_resolution_function_name(iToken, lObjects):
        return classify_resolution_function_name(iToken, lObjects)
    return iToken


def classify_element_resolution(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iToken, lObjects)
    iCurrent = utils.assign_tokens_until_matching_closing_paren(parser.todo, iCurrent, lObjects)

    return iCurrent


def classify_resolution_function_name(iToken, lObjects):

    return utils.assign_next_token(token.resolution_function_name, iToken, lObjects)


def detect_element_resolution(iToken, lObjects):
    if utils.is_next_token('(', iToken, lObjects):
        return True
    return False


def detect_resolution_function_name(iToken, lObjects):
    if detect_escape_value(iToken, lObjects):
        return False
    return True


lEscapeValues = ['(', ')', ';', ':=', 'range', 'bus', 'is', 'open']


def detect_escape_value(iToken, lObjects):
    iTemp = utils.find_next_token(iToken, lObjects) + 1
    if utils.is_next_token_one_of(lEscapeValues, iTemp, lObjects):
        return True
    return False
