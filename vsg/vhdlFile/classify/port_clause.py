
from vsg.token import port_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import port_list


def detect(iToken, lObjects):
    '''
    port_clause ::=
        port ( port_list ) ;
    '''

    if utils.are_next_consecutive_tokens(['port', '('], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('port', token.port_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)

    iCurrent = port_list.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
