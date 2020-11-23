
from vsg.token import generic_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_list


def detect(iToken, lObjects):
    '''
    generic_clause ::=
        generic ( generic_list ) ;
    '''
    if utils.are_next_consecutive_tokens(['generic', '('], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('generic', token.generic_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)

    iCurrent = generic_list.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
